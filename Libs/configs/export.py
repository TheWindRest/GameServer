import redis
import argparse
import json
from Libs import const


config = {
    "Map": "Map.json",
}


def readConfig(configFile):
    fin = open(configFile, 'r', encoding="utf-8")
    return json.load(fin)


def initRedis(configFile):
    redisInfo = configFile.get("redis")
    assert redisInfo

    DBRedis = redis.Redis(**redisInfo)
    if DBRedis.ping():
        print("connect redis succeed!")
    else:
        print("connect redis failed!")
        exit(0)

    return DBRedis


def exportConfig(red):
    path = const.AppPath + r"Libs/configs/jsons/"
    for key, value in config.items():
        filePath = path + value
        file = open(filePath, 'r', encoding="utf-8")
        content = {}
        for _, temp in enumerate(json.load(file)):
            content[temp['ID']] = temp
        red.hset('config', key, json.dumps(content))


parser = argparse.ArgumentParser()
parser.add_argument('--cfg', type=str, default='../../config.json', help='config file')

args = parser.parse_args()
configInfo = readConfig(args.cfg)

DBRedis = initRedis(configInfo)
exportConfig(DBRedis)
