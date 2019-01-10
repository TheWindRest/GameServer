from twisted.internet import task
from Libs.protobuf import CS_GS_pb2
from twisted.python import log
from Libs import error
from CenterServer.Models import match
from Libs import const
from CenterServer.Models import user


def process_register_result(p, zipMsg):
    msgInfo = CS_GS_pb2.AskRegister()
    msgInfo.ParseFromString(zipMsg.data)
    log.msg("recv msg:" + msgInfo.__str__())

    if msgInfo.state == 1:
        p.factory.gateProto = p
        log.msg("Center Register Success!")

        if p.factory.matchTask:
            p.factory.matchTask.stop()
        p.factory.matchTask = task.LoopingCall(match.handleWaiters)
        p.factory.matchTask.start(const.MatchTimeInterval)

        if p.factory.roomTask:
            p.factory.roomTask.stop()
        p.factory.roomTask = task.LoopingCall(p.factory.update)
        p.factory.roomTask.start(const.UpdateTimeInterval)
    else:
        log.msg("Center Register Failed!")


def process_error_msg(p, zipMsg):
    msg = CS_GS_pb2.ErrorMsg()
    msg.ParseFromString(zipMsg.data)
    log.msg("recv msg:" + msg.__str__())

    if msg.errorid == error.ERR_CENTER_ADDRESS:
        print("错误的中心服务器地址")
    elif msg.errorid == error.ERR_USER_LOGOUT:
        mail = zipMsg.mail
        userInfo = user.getUser(mail)
        if userInfo:
            roomId = userInfo.get("roomid")
            house = p.factory.roomDict.get(roomId)
            if house:
                house.deletePlayer(mail)


def process_user_info(p, zipMsg):
    msgInfo = CS_GS_pb2.UserInfo()
    msgInfo.ParseFromString(zipMsg.data)
    log.msg("recv msg:" + msgInfo.__str__())

    userMail = zipMsg.mail
    print(userMail)
    msgInfo.name = "hahaha"

    p.transmitMessage(zipMsg, msgInfo)


def process_start_match(p, zipMsg):
    msgInfo = CS_GS_pb2.StartMatch()
    msgInfo.ParseFromString(zipMsg.data)
    log.msg("recv msg:" + msgInfo.__str__())

    mail = msgInfo.mail
    waiters = p.factory.matchList
    if mail not in waiters:
        p.factory.matchList.append(mail)
        msgInfo.result = 1
    else:
        msgInfo.result = 0
    p.transmitMessage(zipMsg, msgInfo)


def process_transform_sync(p, zipMsg):
    msgInfo = CS_GS_pb2.TransformSync()
    msgInfo.ParseFromString(zipMsg.data)
    log.msg("recv msg:" + msgInfo.__str__())

    house = p.factory.roomDict.get(msgInfo.roomid)
    if house:
        house.transformSync(msgInfo)
    else:
        msgInfo = CS_GS_pb2.ErrorMsg()
        msgInfo.errorid = error.ERR_TRANSFORM_SYNC
        p.transmitMessage(zipMsg, msgInfo)


def process_shoot_bullet(p, zipMsg):
    msgInfo = CS_GS_pb2.ShootBullet()
    msgInfo.ParseFromString(zipMsg.data)
    log.msg("recv msg:" + msgInfo.__str__())

    house = p.factory.roomDict.get(msgInfo.roomid)
    if house:
        house.shootBullet(msgInfo)
    else:
        msgInfo = CS_GS_pb2.ErrorMsg()
        msgInfo.errorid = error.ERR_SHOOT_BULLET
        p.transmitMessage(zipMsg, msgInfo)


def process_take_damage(p, zipMsg):
    msgInfo = CS_GS_pb2.TakeDamage()
    msgInfo.ParseFromString(zipMsg.data)
    log.msg("recv msg:" + msgInfo.__str__())

    house = p.factory.roomDict.get(msgInfo.roomid)
    if house:
        house.takeDamage(msgInfo)
    else:
        msgInfo = CS_GS_pb2.ErrorMsg()
        msgInfo.errorid = error.ERR_MSG_ERROR
        p.transmitMessage(zipMsg, msgInfo)
