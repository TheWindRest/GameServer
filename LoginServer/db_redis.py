import redis


def initRedis(configFile):
    redisInfo = configFile.get("redis")
    assert redisInfo

    global DBRedis
    DBRedis = redis.Redis(**redisInfo)
    if DBRedis.ping():
        print("connect redis succeed!")
    else:
        print("connect redis failed!")
        exit(0)
