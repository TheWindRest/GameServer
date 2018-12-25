import json
import copy
from Libs import const
from LoginServer import db_redis


user = {
    "name":         "",
    "password":     "",
    "mail":         "",
    "token":        "",
    "platform":     "",
}


def getKeyInRedis(mail):
    return const.UserPrefix + mail


def createUser(mail, password):
    assert(type(mail) == str)

    newUser = copy.deepcopy(user)
    newUser["mail"] = mail
    newUser["password"] = password
    packDt = {k: json.dumps(v) for k, v in newUser.items()}
    db_redis.DBRedis.hmset(getKeyInRedis(mail), packDt)
    return newUser


def getUser(mail):
    assert(type(mail) == str)

    user = db_redis.DBRedis.hgetall(getKeyInRedis(mail))
    if user:
        return({k.decode(): json.loads(v) for k, v in user.items()})
    else:
        return None


def getUserByMail(mail, password):
    userInfo = getUser(mail)
    if userInfo:
        userPassword = userInfo.get("password")
        if userPassword == password:
            return userInfo
        else:
            return None
    else:
        return createUser(mail, password)


def getMail(token):
    assert(type(token) == str)

    mail = db_redis.DBRedis.hget(const.TokenDict, token)
    return eval(mail)


def getUserByToken(token):
    mail = getMail(token)
    if mail != "" and mail is not None:
        return getUser(mail)
    else:
        return None
