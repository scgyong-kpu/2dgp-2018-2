import json
from pico2d import *

class WallRect:
    def __init__(self, rect):
        self.bb = tuple(rect)
    def get_bb(self):
        return self.bb

class Wall:
    def __init__(self):
        f = open('wall.json')
        d = json.load(f)
        f.close()
        self.__dict__.update(d)
        # print(self.__dict__)
        self.left = WallRect(self.left_l)
        self.right = WallRect(self.right_l)
        self.top = WallRect(self.top_l)
        self.image = load_image(self.image_name)
        self.bg_pattern = load_image(self.bg_pattern_name)
        self.bg_index = -1
    def update(self):
        pass
    def draw(self):
        cw = get_canvas_width()
        ch = get_canvas_height()
        pw, ph = 64, 64
        if self.bg_index >= 0:
            ix = self.bg_index % 14
            iy = self.bg_index // 14
            y = 0
            while y < ch:
                x = 0
                while x < cw:
                    self.bg_pattern.clip_draw_to_origin(ix * pw, iy * ph, pw, ph, x, y)
                    x += ph
                y += pw
        for co in self.coords:
            self.image.clip_draw_to_origin(co[0], co[1], co[2], co[3], co[4], co[5], co[2], co[3])
    def drawRight(self):
        for co in self.coordsRight:
            self.image.clip_draw_to_origin(co[0], co[1], co[2], co[3], co[4], co[5], co[2], co[3])
    def didBounce(self, ball):
        ret = False
        if ball.intersection(self.left) != None:
            ret = ball.bounceRight()
        if ball.intersection(self.right) != None:
            ret = ball.bounceLeft()
        if ball.intersection(self.top) != None:
            ret = ball.bounceDown()
        if ball.y < 0:
            ret = ball.bounceUp()
        return ret
