from Libs import base_protocol
from LoginServer.Handlers import LoginService
from Libs.protobuf import GC_LS_pb2, GS_LS_pb2
import time


class ClientProtocol(base_protocol.GoogleProtocol):
    userInfo = {}

    REQUEST_HANDLERS = {
        GC_LS_pb2.GC2LS_AskLogin: LoginService.process_user_login,
    }

    def connectionMade(self):
        print('Client->Login Start!', self.transport.getPeer())

    def connectionLost(self, reason):
        mail = self.userInfo.get("mail")
        if mail:
            if self.factory.users.get(mail) == self:
                self.factory.users.pop(mail)
                self.factory.offlineUsers[mail] = int(time.time())

        print('[%s] Client->Login Lost!' % self.__class__.__name__, reason.getErrorMessage())


class GateProtocol(base_protocol.GoogleProtocol):
    gateInfo = {}

    REQUEST_HANDLERS = {
        GS_LS_pb2.GS2LS_AskRegister: LoginService.process_gate_register,
        GS_LS_pb2.GS2LS_CheckLogin: LoginService.process_check_login,
    }

    def connectionMade(self):
        print('Gate->Login Start!', self.transport.getPeer())

    def connectionLost(self, reason):
        host = self.gateInfo.get("host")
        if self.factory.gateServers.get(host) == self:
            self.factory.gateServers.pop(host)
        print('[%s] Gate->Login Lost!' % self.__class__.__name__, reason.getErrorMessage())
