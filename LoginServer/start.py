from twisted.internet import reactor
import argparse
import json

from LoginServer import db_redis
from LoginServer import server


def readConfig(configFile):
    fin = open(configFile, 'r', encoding="utf-8")
    return json.load(fin)


parser = argparse.ArgumentParser()
parser.add_argument('--cfg', type=str, default='../config.json', help='config file')
parser.add_argument('--name', type=str, help='server')

args = parser.parse_args()
configInfo = readConfig(args.cfg)

db_redis.initRedis(configInfo)
server.startGateFactory(configInfo)
server.startClientFactory(configInfo)
reactor.run()
