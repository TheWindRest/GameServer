import numpy as np
from Libs import const
from CenterServer.Models import entity


class Player(entity.Entity):
    name = None
    active = False
    weapon = None
    bullet = 100
    lastShootTime = 0

    def __init__(self, mail, name):
        entity.Entity.__init__(self, mail)
        self.name = name

    def update(self, timeInterval):
        direction = np.array(self.rotation, dtype=np.float)
        currentPos = np.array(self.position, dtype=np.float)
        velocity = direction * self.speed * const.MoveSpeed
        currentPos += velocity * timeInterval
        self.position = currentPos.__array__()
