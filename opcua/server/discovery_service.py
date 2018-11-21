
from opcua import ua

class LocalDiscoveryService(object):

    class ServerDesc(object):
        def __init__(self, appDesc, uaDiscoveryConfiguration=None):
            self.applicationDescription = appDesc
            self.discoveryConfiguration = uaDiscoveryConfiguration

    def __init__(self):
        self._known_servers = {}

    def find_servers(self, params):
        servers = []
        for srvDesc in self._known_servers.values():
            # No Filtering.
            if not params.ServerUris:
                servers.append(srvDesc.applicationDescription)
                continue
            # Filter on server uris.
            srv_uri = srvDesc.applicationDescription.ApplicationUri.split(":")
            for uri in params.ServerUris:
                uri = uri.split(":")
                if srv_uri[:len(uri)] == uri:
                    servers.append(srvDesc.applicationDescription)
                    break
        return servers

    def register_server(self, registeredServer, uaDiscoveryConfiguration=None):
        assert(isinstance(registeredServer, ua.uaprotocol_auto.RegisteredServer))
        appDesc = ua.ApplicationDescription()
        appDesc.ApplicationUri = registeredServer.ServerUri
        appDesc.ProductUri = registeredServer.ProductUri
        # FIXME: select name from client locale
        appDesc.ApplicationName = registeredServer.ServerNames[0]
        appDesc.ApplicationType = registeredServer.ServerType
        appDesc.DiscoveryUrls = registeredServer.DiscoveryUrls
        # FIXME: select discovery uri using reachability from client network
        appDesc.GatewayServerUri = registeredServer.GatewayServerUri
        self.add_server_description(appDesc, uaDiscoveryConfiguration)

    def add_server_description(self, appDesc, uaDiscoveryConfiguration=None):
        assert(isinstance(appDesc, ua.uaprotocol_auto.ApplicationDescription))
        srvDesc = LocalDiscoveryService.ServerDesc(appDesc, uaDiscoveryConfiguration)
        self._known_servers[appDesc.ApplicationUri] = srvDesc
        
    def register_server2(self, params):
        return self.register_server(params.Server, params.DiscoveryConfiguration)
