from pico2d import *
import game_world as gw
# 44x22
# 58x36
# 29,18
# x-29,y-4
# x+15,y+18
class Brick:
    image = None
    def __init__(self, x, y, t):
        self.x, self.y = x, y
        self.type = t
        if t >= 9:
            self.life = 5
        else:
            self.life = 1
        self.w = 10
        self.h = 10
        self.score = 1
        if Brick.image == None:
            Brick.image = load_image('bricks.png')
    def update(self):
        pass
    def draw(self):
        index = self.type - 1
        if self.type == 9:
            index = 8 + self.life
        elif self.type == 10:
            index = 12 + self.life
        # print(index, self.x, self.y)
        self.image.clip_draw(58 * index, 0, 58, 36, self.x, self.y)
    def get_bb(self):
        return self.x-29, self.y-4, self.x+15, self.y+18
    def didBounce(self, ball):
        t = ball.intersection(self)
        if t == None:
            return False
        w, h = t
        if w > h:
            ball.bounceVert()
        else:
            ball.bounceHorz()
        self.life -= 1
        if self.life == 0:
            gw.remove_object(self)
        return True



