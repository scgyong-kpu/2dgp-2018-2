import os.path
from pico2d import *

FONT_1, FONT_2 = range(2)
buttons = []
labels = []

_FONT_FILES = [ \
    "../res/ConsolaMalgun.ttf", \
    "../res/origa_m_p.ttf" \
]
_fonts = {}

def getFont(idx, size):
    global _fonts
    key = str(idx) + '_' + str(size)
    if key in _fonts:
        print("Reuse font:", key)
        return _fonts[key]
    file = _FONT_FILES[idx]
    _fonts[key] = load_font(file, size)
    print("Font created for:", file, size)
    return _fonts[key]

def loadIfExists(file):
    if os.path.isfile(file):
        return load_image(file)
    return None

class Label:
    def __init__(self, text, x, y, size = 20, fontIndex = 0):
        self.text = text
        self.x, self.y = x, y
        self.color = (0, 0, 0)
        self.font = getFont(fontIndex, size)
    def draw(self):
        self.font.draw(self.x, self.y, self.text, self.color)

class Button:
    def __init__(self, file, x, y, onClick = None, context = ''):
        self.image_n = loadIfExists(file + '.png')
        self.image_h = loadIfExists(file + '_h.png')
        self.image_p = loadIfExists(file + '_p.png')
        self.x, self.y = x, y
        self.image = self.image_n
        self.captures = False
        self.pressed = False
        self.onClick = onClick
        self.context = context
    def draw(self):
        self.image.draw(self.x, self.y)
    def hits(self, x, y):
        hw, hh = self.image_n.w // 2, self.image_n.h // 2
        if x < self.x - hw: return False
        if x > self.x + hw: return False
        if y < self.y - hh: return False
        if y > self.y + hw: return False
        return True
    def handle_event(self, et, x, y):
        over = self.hits(x, y)
        if not over:
            print("No hit", self.captures)
            if not self.captures:
                self.setImage(self.image_n)
                return False

        if et == SDL_MOUSEBUTTONDOWN:
            self.setImage(self.image_p)
            self.captures = True
            return True
        elif et == SDL_MOUSEBUTTONUP:
            self.captures = False
            if over:
                self.fire()
        image = self.image_n
        if self.captures: 
            image = self.image_p if over else self.image_h
        elif over:
            image = self.image_h
        self.setImage(image)
        return True

    def setImage(self, image):
        if image != None:
            self.image = image

    def fire(self):
        print("Fire")
        if self.onClick == None:
            return
        self.onClick(self.context)


def update():
    pass

def draw():
    for b in buttons:
        b.draw()
    for l in labels:
        l.draw()

capture_button = None
def handle_event(e):
    global capture_button
    EVENTS = [ SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP ]
    if not e.type in EVENTS:
        return
    x,y = e.x, get_canvas_height() - e.y
    if capture_button != None:
        if capture_button.handle_event(e.type, x, y):
            return
        else:
            capture_button = None
    for b in buttons:
        if b.hits(x, y):
            capture_button = b
            print("Now capture_button:", b)
            b.handle_event(e.type, x, y)
            break

