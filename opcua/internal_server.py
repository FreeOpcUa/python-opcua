"""
Internal server to be used on server side
"""
import uuid
import logging
from threading import RLock

from opcua import ua
from opcua import utils
from opcua.address_space import AddressSpace
from opcua.standard_address_space_part3 import create_standard_address_space_Part3
from opcua.standard_address_space_part4 import create_standard_address_space_Part4
from opcua.standard_address_space_part5 import create_standard_address_space_Part5
from opcua.standard_address_space_part8 import create_standard_address_space_Part8
from opcua.standard_address_space_part9 import create_standard_address_space_Part9
from opcua.standard_address_space_part10 import create_standard_address_space_Part10
from opcua.standard_address_space_part11 import create_standard_address_space_Part11
from opcua.standard_address_space_part13 import create_standard_address_space_Part13

class Session(object):
    _counter = 10
    _auth_counter = 1000
    def __init__(self):
        self.session_id = ua.NodeId(self._counter)
        Session._counter += 1
        self.authentication_token = ua.NodeId(self._auth_counter)
        Session._auth_counter += 1
        self.nonce = utils.create_nonce() 

    def __str__(self):
        return "InternalSession(id:{}, auth_token:{})".format(self.session_id, self.authentication_token)


class InternalServer(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.endpoints = []
        self.sessions = {}
        self._channel_id_counter = 5
        self.aspace = AddressSpace()
        create_standard_address_space_Part3(self.aspace)
        create_standard_address_space_Part4(self.aspace)
        create_standard_address_space_Part5(self.aspace)
        create_standard_address_space_Part8(self.aspace)
        create_standard_address_space_Part9(self.aspace)
        create_standard_address_space_Part10(self.aspace)
        create_standard_address_space_Part11(self.aspace)
        create_standard_address_space_Part13(self.aspace)
        self.channels = {}
        self._lock = RLock()

    def open_secure_channel(self, params, currentchannel=None):
        self.logger.info("open secure channel")
        with self._lock:
            if params.RequestType == ua.SecurityTokenRequestType.Issue:
                channel = ua.OpenSecureChannelResult()
                channel.SecurityToken.TokenId = 13 #random value
                channel.SecurityToken.ChannelId = self._channel_id_counter
                channel.SecurityToken.RevisedLifetime = params.RequestedLifetime 
                self._channel_id_counter += 1
            else:
                channel = self.channels[currentchannel.SecurityToken.ChannelId]
            channel.SecurityToken.TokenId += 1
            channel.SecurityToken.CreatedAt = ua.DateTime()
            channel.SecurityToken.RevisedLifetime = params.RequestedLifetime
            channel.ServerNonce = uuid.uuid4().bytes + uuid.uuid4().bytes
            self.channels[channel.SecurityToken.ChannelId] = channel
            return channel

    def add_endpoint(self, endpoint):
        with self._lock:
            self.endpoints.append(endpoint)

    def get_endpoints(self, params=None):
        #FIXME check params
        with self._lock:
            return self.endpoints[:]

    def create_session(self, params):
        self.logger.info("create session")
        with self._lock:
            session = Session()
            self.sessions[session.session_id] = session
            self.logger.info("Create session request, created session: %s", session)

            result = ua.CreateSessionResult()
            result.SessionId = session.session_id
            result.AuthenticationToken = session.authentication_token 
            result.RevisedSessionTimeout = params.RequestedSessionTimeout
            result.MaxRequestMessageSize = 65536
            result.ServerNonce = session.nonce
            result.ServerEndpoints = self.endpoints[:]

            return result

    def close_session(self, session, delete_subs):
        self.logger.info("close session")
        with self._lock:
            if not session.SessionId in self.sessions:
                self.logger.warn("session id %s is invalid: available sessions are %s", session.SessionId, self.sessions)
                return
            self.sessions.pop(session.SessionId)

    def activate_session(self, session, params):
        self.logger.info("activate session")
        with self._lock:
            result = ua.ActivateSessionResult()
            if not session:
                result.Results = [ua.StatusCode(ua.StatusCodes.BadSessionIdInvalid)]
                return result
            result.ServerNonce = self.sessions[session.SessionId].nonce
            for _ in params.ClientSoftwareCertificates:
                result.Results.append(ua.StatusCode())
            return result

    def read(self, params):
        return self.aspace.read(params)

    def write(self, params):
        return self.aspace.write(params)

    def browse(self, params):
        return self.aspace.browse(params)

    def translate_browsepaths_to_nodeids(self, params):
        return self.aspace.translate_browsepaths_to_nodeids(params)

    def add_nodes(self, params):
        return self.aspace.add_nodes(params)


