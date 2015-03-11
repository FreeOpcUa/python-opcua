"""
Internal server to be used on server side
"""
import uuid
import logging

from opcua import ua
from opcua import utils
from opcua.address_space import AddressSpace

class Session(object):
    _counter = 10
    _auth_counter = 1000
    def __init__(self):
        self.session_id = ua.NodeId(self._counter)
        self._counter += 1
        self.authentication_token = ua.NodeId(self._auth_counter)
        self._auth_counter += 1
        self.nonce = utils.create_nonce() 


class InternalServer(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.endpoints = []
        self.sessions = {}
        self._channel_id_counter = 1
        self.aspace = AddressSpace()
        self.channels = {}

    def open_secure_channel(self, params, current=None):
        #handle data
        if params.RequestType == ua.SecurityTokenRequestType.Issue:
            channel = ua.OpenSecureChannelResult()
            channel.SecurityToken.ChannelId = self._channel_id_counter
            self._channel_id_counter += 1
        else:
            channel = self.channels[current]
        channel.SecurityToken.TokenId += 1
        channel.SecurityToken.CreatedAt = ua.DateTime()
        channel.SecurityToken.RevisedLifeTime = params.RequestedLifetime
        channel.ServerNonce = uuid.uuid4().bytes + uuid.uuid4().bytes
        return channel

    def add_endpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def get_endpoints(self, params=None):
        #FIXME check params
        return self.endpoints 

    def create_session(self, params):
        session = Session()
        self.sessions[session.session_id] = session

        result = ua.CreateSessionResult()
        result.SessionId = session.session_id
        result.AuthenticationToken = session.authentication_token 
        result.RevisedSessionTimeout = params.RequestedSessionTimeout
        result.MaxRequestMessageSize = 65536
        result.ServerNonce = session.nonce
        result.endpoints = self.get_endpoints()

        return result



