from twisted.python import log
from Libs import base_protocol
from CenterServer.Handlers import CenterService
from Libs.protobuf import CS_GS_pb2


class GateProtocol(base_protocol.GoogleProtocol):

    REQUEST_HANDLERS = {
        CS_GS_pb2.CS2GS_AskRegister: CenterService.process_register_result,
        CS_GS_pb2.GS2CS_Error: CenterService.process_error_msg,
        CS_GS_pb2.CS2GS_UserInfo: CenterService.process_user_info,
        CS_GS_pb2.CS2GS_StartMatch: CenterService.process_start_match,
        CS_GS_pb2.CS2GS_TransformSync: CenterService.process_transform_sync,
        CS_GS_pb2.CS2GS_ShootBullet: CenterService.process_shoot_bullet,
        CS_GS_pb2.CS2GS_TakeDamage: CenterService.process_take_damage,
    }

    def connectionMade(self):
        msgInfo = CS_GS_pb2.AskRegister()
        msgInfo.state = 0
        for key in self.REQUEST_HANDLERS:
            msgInfo.msgList.append(key)
        self.sendMessage(msgInfo)
        log.msg('Center->Gate Start!', self.transport.getPeer())

    def connectionLost(self, reason):
        log.msg('[%s] Center->Gate Lost!' % self.__class__.__name__, reason.getErrorMessage())

    def handleMessage(self, msgID, Data):
        zipMsg = CS_GS_pb2.TransmitMsg()
        zipMsg.ParseFromString(Data)

        handler = self.REQUEST_HANDLERS.get(msgID)
        if handler:
            handler(self, zipMsg)

    def transmitMessage(self, zipMsg, body):
        zipMsg.msgid = body.msgid
        zipMsg.data = body.SerializeToString()
        self.sendMessage(zipMsg)
