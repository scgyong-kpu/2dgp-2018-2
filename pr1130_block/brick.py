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
        self.w = 44
        self.h = 22
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
        self.image.clip_draw(58 * index, 0, 58, 36, self.x + 7, self.y - 7)
        # draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-22, self.y-11, self.x+22, self.y+11
    def didBounce(self, ball):
        t = ball.intersection(self)
        if t == None:
            return False
        w, h = t
        # print("%.2f, %.2f" % (w, h), "b<%d,%d,%d,%d>" % self.get_bb(), "[%d,%d,%d,%d]" % ball.get_bb() )
        if w > h:
            ball.bounceVert()
        else:
            ball.bounceHorz()
        self.life -= 1
        if self.life == 0:
            gw.remove_object(self)
        return True



