from pico2d import *
# 44x22
# 58x36
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
        print(index, self.x, self.y)
        self.image.clip_draw(58 * index, 0, 58, 36, self.x, self.y)



