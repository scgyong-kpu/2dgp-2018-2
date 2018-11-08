from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('../res/futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.width = self.image.w
        self.height = self.image.h
        self.x, self.y = 0, 0
        self.target = None
    def draw(self):
        self.image.clip_draw_to_origin(self.x, self.y, self.cw, self.ch, 0, 0)
    def update(self):
        if self.target == None: 
            return
        self.x = clamp(0, int(self.target.x - self.cw // 2), self.width - self.cw)
        self.y = clamp(0, int(self.target.y - self.ch // 2), self.height - self.ch)
        # print(self.x, self.y, self.cw, self.ch, 0, 0)

class InfiniteBackground:
    def __init__(self):
        self.image = load_image('../res/futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.width = self.image.w
        self.height = self.image.h
        self.x, self.y = 0, 0
        self.target = None
    def draw(self):
        self.image.clip_draw_to_origin(self.x1, self.y1, self.w1, self.h1, 0, 0)
    def update(self):
        if self.target == None: 
            return
        self.x = int(self.target.x - self.cw // 2)
        self.y = int(self.target.y - self.ch // 2)
        self.x1 = self.x % self.width
        self.y1 = self.y % self.height
        self.w1 = self.width - self.x1
        self.h1 = self.height - self.y1
        # print(self.x, self.y, self.cw, self.ch, 0, 0)
