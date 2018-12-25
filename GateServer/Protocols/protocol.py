from twisted.python import log
from Libs import base_protocol
from GateServer.Handlers import GateService
from Libs.protobuf import GC_GS_pb2, GS_LS_pb2, CS_GS_pb2


class ClientProtocol(base_protocol.GoogleProtocol):
    userInfo = {}

    REQUEST_HANDLERS = {
        GC_GS_pb2.GC2GS_TokenLogin: GateService.process_user_login,
    }

    def connectionMade(self):
        log.msg('Client->Gate Start!', self.transport.getPeer())

    def connectionLost(self, reason):
        mail = self.userInfo.get("mail")

        if self.factory.users.get(mail) == self:
            self.factory.users.pop(mail)
        log.msg('[%s] Client->Gate Lost!' % self.__class__.__name__, reason.getErrorMessage())


class LoginProtocol(base_protocol.GoogleProtocol):

    REQUEST_HANDLERS = {
        GS_LS_pb2.GS2LS_AskRegister: GateService.process_register_result,
        GS_LS_pb2.GS2LS_CheckLogin: GateService.process_check_result,
    }

    def connectionMade(self):
        msgInfo = GS_LS_pb2.AskRegister()
        msgInfo.host = self.factory.listenIP
        msgInfo.port = self.factory.listenPort
        msgInfo.state = 0
        self.sendMessage(msgInfo)
        log.msg('Gate->Login Start!', self.transport.getPeer())

    def connectionLost(self, reason):
        log.msg('[%s] Gate->Login Lost!' % self.__class__.__name__, reason.getErrorMessage())


class CenterProtocol(base_protocol.GoogleProtocol):
    centerInfo = {}

    REQUEST_HANDLERS = {
        CS_GS_pb2.CS2GS_AskRegister: GateService.process_center_register,
    }

    def connectionMade(self):
        log.msg('Center->Gate Start!', self.transport.getPeer())

    def connectionLost(self, reason):
        log.msg('[%s] Center->Gate Lost!' % self.__class__.__name__, reason.getErrorMessage())    
