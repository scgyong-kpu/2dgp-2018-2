import json
from pico2d import *

class Wall:
    LEFT = 50
    BOTTOM = 50
    TOP = 550
    RIGHT = 450
    image = None
    coords = None
    def __init__(self):
        if Wall.image == None:
            Wall.image = load_image('wall.png')
        if Wall.coords == None:
            f = open('wall.json')
            Wall.coords = json.load(f)
            f.close()
    def update(self):
        pass
    def draw(self):
        for co in self.coords:
            print(co)
            self.image.clip_draw_to_origin(co[0], co[1], co[2], co[3], co[4], co[5], co[2], co[3])
    def didBounce(self, ball):
        ret = False
        if (ball.x < Wall.LEFT or ball.x > Wall.RIGHT):
            ball.angle = math.pi - ball.angle
            ret = True
        if (ball.y < Wall.BOTTOM or ball.y > Wall.TOP):
            ball.angle = -ball.angle
            ret = True
        if ret:
            ball.angle = ball.angle % (2 * math.pi)
            print('angle is now:', ball.angle)
        return ret
