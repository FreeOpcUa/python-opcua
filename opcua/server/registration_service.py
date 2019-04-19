
import logging
from threading import Lock
from functools import partial

try:
    from urllib.parse import urlparse
except ImportError:  # support for python2
    from urlparse import urlparse

from opcua import ua
from opcua.client.client import Client

class RegistrationService(object):
    DEF_DISCOVERY_URL = "opc.tcp://localhost:4840" # By OPC-UA specification.
    MAX_CLIENT = 32 # [-] Max. number of simultaneous client connections.
    DEF_REGINT = 60 # [sec] Default re-registration interval.
    MIN_REGINT = 10 # [sec] Minimal re-registration interval.

    # FIXME monitor connection to serverToRegister.

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._registration_clients = []
        self._lock = Lock()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with self._lock:
            for client in self._registration_clients:
                client.disconnect()
            self._registration_clients = []

    def register_to_discovery(self, serverToRegister=None, discoveryUrl=DEF_DISCOVERY_URL, period=DEF_REGINT):
        """
        Register to an OPC-UA Discovery server. Registering must be renewed at
        least every 10 minutes, so this method will use our asyncio thread to
        re-register every period seconds
        if period is 0 registration is not automatically renewed
        """
        # Detect accidental registration loops.
        if len(self._registration_clients) >= self.MAX_CLIENT:
            raise Exception('Max. discovery servers reached: {:d}'.format(self.MAX_CLIENT))
        # Prevent multiple registrations to one discovery server.
        netloc = urlparse(discoveryUrl).netloc
        for client in self._registration_clients:
            if client.server_url.netloc != netloc:
                continue
            raise Exception('Already registering to discovery server: {:s}'.format(discoveryUrl))
        # Create and store client connection to discovery server.
        registrationClient = Client(discoveryUrl)
        registrationClient.connect()
        self._registration_clients.append(registrationClient)
        self._renew_registration(serverToRegister, registrationClient, period=period)

    def unregister_to_discovery(self, discoveryUrl=DEF_DISCOVERY_URL):
        """
        Unregister from OPC-UA Discovery server.
        """
        # FIXME: is there really no way to deregister?
        netloc = urlparse(discoveryUrl).netloc
        with self._lock:
            for client in self._registration_clients[:]:
                if client.server_url.netloc != netloc:
                    continue
                self._registration_clients.remove(client)
                client.disconnect()
                break

    # This method is called once from the main thread.
    # Subsequent periodic calls are from asyncio loop.
    def _renew_registration(self, serverToRegister, registrationClient, period=DEF_REGINT):
        # Send registration request to discovery server.
        try:
            with self._lock: # So we don't client.disconnect() from main thread.
                if registrationClient not in self._registration_clients:
                    return
                self._register_server(serverToRegister, registrationClient)
        except (BrokenPipeError, OSError) as e:
            self.logger.info("Discovery server registration failure: {:s}".format(str(e)))
            return # TODO handle connection loss (retry x times?).
        except TimeoutError:
            self.logger.info("Discovery server registration timeout: {:s}".format(str(e)))
        # Decide whether to schedule a registration renewal.
        if period == 0:
            return # no periodic registrations.
        elif not serverToRegister.iserver.is_running():
            return # won't happen as we currently use serverToRegister's own event loop.
        else:
            self._schedule_registration(serverToRegister, registrationClient, period)

    def _schedule_registration(self, serverToRegister, registrationClient, period=DEF_REGINT):
        # Schedule automatic re-registrations every <period> sec.
        if (period < RegistrationService.MIN_REGINT):
            raise ValueError("Period must be larger than {:d} [sec].".format(RegistrationService.MIN_REGINT))
        renew_cb = partial(self._renew_registration,
            serverToRegister = serverToRegister,
            registrationClient = registrationClient,
            period = period
        )
        # Piggyback on the serverToRegister's asyncio loop.
        serverToRegister.iserver.loop.call_later(period, renew_cb)

    @staticmethod
    def _register_server(serverToRegister, registrationClient, uaDiscoveryConfiguration=None):
        """
        Register serverToRegister to discovery server
        if uaDiscoveryConfiguration is provided, the newer register_server2 service call is used
        """
        uaRegSrv = ua.RegisteredServer()
        uaRegSrv.ServerUri = serverToRegister.get_application_uri()
        uaRegSrv.ProductUri = serverToRegister.product_uri
        uaRegSrv.DiscoveryUrls = [serverToRegister.endpoint.geturl()]
        uaRegSrv.ServerType = serverToRegister.application_type
        uaRegSrv.ServerNames = [ua.LocalizedText(serverToRegister.name)]
        uaRegSrv.IsOnline = serverToRegister.iserver.is_running()
        if uaDiscoveryConfiguration:
            params = ua.RegisterServer2Parameters()
            params.Server = uaRegSrv
            params.DiscoveryConfiguration = uaDiscoveryConfiguration
            return registrationClient.uaclient.register_server2(params)
        else:
            return registrationClient.uaclient.register_server(uaRegSrv)
