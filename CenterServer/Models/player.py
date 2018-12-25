import numpy as np
from Libs import const


class Player():
    mail = None
    active = False
    speed = 0
    rotation = [0, 0, 0]
    position = [0, 0, 0]
    health = 100

    lastShootTime = 0

    def __init__(self, mail):
        self.mail = mail

    def update(self, timeInterval):
        direction = np.array(self.rotation, dtype=np.float)
        currentPos = np.array(self.position, dtype=np.float)
        velocity = direction * self.speed * const.MoveSpeed
        currentPos += velocity * timeInterval
        self.position = currentPos.__array__()