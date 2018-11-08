from pico2d import *

class ParallexLayer:
    def __init__(self, imageName, speed):
        self.image = load_image(imageName)
        self.w, self.h = self.image.w, self.image.h
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.speed = speed

    def draw(self):
        self.image.clip_draw_to_origin(self.x1, 0, self.w1, self.h, 0, 0)
        self.image.clip_draw_to_origin(self.x2, 0, self.w2, self.h, self.w1, 0)

    def update(self, x):
        self.x1 = int(x * self.speed) % self.image.w
        self.w1 = self.image.w - self.x1

        self.x2 = 0
        self.w2 = self.cw - self.w1 

class ParallexBackground:
    def __init__(self):
        self.layers = [\
            ParallexLayer('../res/b0.png', 0.3), \
            ParallexLayer('../res/b1.png', 0.7), \
            ParallexLayer('../res/b2.png', 1.0), \
        ]
        self.min_x, self.min_y = 0, 100
        self.max_x, self.max_y = 20000, 100,
        self.x, self.y = 0, 0
        self.target = None
    def clamp(self, o):
        o.x = clamp(self.min_x, o.x, self.max_x) 
        o.y = clamp(self.min_y, o.y, self.max_y) 
    def draw(self):
        for l in self.layers: l.draw()
    def update(self):
        self.x = int(self.target.x - 100)
        for l in self.layers: l.update(self.x)

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
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 20000, 2000,
        self.x, self.y = 0, 0
        self.target = None
    def clamp(self, o):
        o.x = clamp(self.min_x, o.x, self.max_x) 
        o.y = clamp(self.min_y, o.y, self.max_y) 
    def draw(self):
        self.image.clip_draw_to_origin(self.x3, self.y3, self.w3, self.h3, 0, 0)
        self.image.clip_draw_to_origin(self.x2, self.y2, self.w2, self.h2, 0, self.h3)
        self.image.clip_draw_to_origin(self.x4, self.y4, self.w4, self.h4, self.w3, 0)
        self.image.clip_draw_to_origin(self.x1, self.y1, self.w1, self.h1, self.w3, self.h3)

    def update(self):
        if self.target == None: 
            return
        self.x = int(self.target.x - self.cw // 2)
        self.y = int(self.target.y - self.ch // 2)
        self.x3 = self.x % self.width
        self.y3 = self.y % self.height
        self.w3 = self.width - self.x3
        self.h3 = self.height - self.y3

        self.x2 = self.x3
        self.y2 = 0
        self.w2 = self.w3
        self.h2 = self.ch - self.h3

        self.x4 = 0
        self.y4 = self.y3
        self.w4 = self.cw - self.w3 
        self.h4 = self.h3

        self.x1 = 0 
        self.y1 = 0 
        self.w1 = self.w4 
        self.h1 = self.h2

