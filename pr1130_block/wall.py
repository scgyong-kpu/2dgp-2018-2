import json
from pico2d import *

class Wall:
    def __init__(self):
        f = open('wall.json')
        d = json.load(f)
        f.close()
        self.__dict__.update(d)
        self.image = load_image('wall.png')
    def update(self):
        pass
    def draw(self):
        for co in self.coords:
            self.image.clip_draw_to_origin(co[0], co[1], co[2], co[3], co[4], co[5], co[2], co[3])
    def didBounce(self, ball):
        ret = False
        if (ball.x < self.left or ball.x > self.right):
            ball.angle = math.pi - ball.angle
            ret = True
        if (ball.y < self.bottom or ball.y > self.top):
            ball.angle = -ball.angle
            ret = True
        if ret:
            ball.angle = ball.angle % (2 * math.pi)
            print('angle is now:', ball.angle)
        return ret
