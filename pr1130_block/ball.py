import game_framework
from game_object import *

class Ball(GameObject):
    PPS = 100
    def __init__(self, x, y, dx, dy):
        super(Ball, self).__init__()
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.size = 22
        self.w, self.h = 22, 22
        self.angle = 1.0
        self.speed = 3.0
        self.image = self.init_image(Ball, 'ball.png', 3, 4)
    def update(self):
        self.update_frame()
        distance = game_framework.frame_time * Ball.PPS * self.speed
        dx = distance * math.cos(self.angle)
        dy = distance * math.sin(self.angle)
        self.x += dx
        self.y += dy
    def draw(self):
        # print(self.frame, self._count)
        self.draw_frame()
    def bounceLeft(self):
        q = self.angle // (math.pi / 2)
        ret = False
        if q == 0:
            self.angle = math.pi - self.angle
            ret = True
        if q == 3:
            a = self.angle
            self.angle = 3 * math.pi - self.angle
            ret = True
            # print('bl,q3', a, '->', self.angle)
        return ret
    def bounceRight(self):
        q = self.angle // (math.pi / 2)
        ret = False
        if q == 1:
            self.angle = math.pi - self.angle
            ret = True
        if q == 2:
            self.angle = 3 * math.pi - self.angle
            ret = True
        return ret
    def bounceUp(self):
        # print('bup', self.angle)
        q = self.angle // (math.pi / 2)
        ret = False
        if q == 2 or q == 3:
            self.bounceVert()
            ret = True
        return ret
    def bounceDown(self):
        q = self.angle // (math.pi / 2)
        ret = False
        if q == 0 or q == 1:
            self.bounceVert()
            ret = True
        return ret
    def bounceVert(self):
        a = self.angle
        self.angle = 2 * math.pi - self.angle
        # print(a, '->', self.angle)
    def bounceHorz(self):
        c = self.angle // (math.pi)
        m = 1 if c == 0 else 3
        self.angle = m * math.pi - self.angle
