from pico2d import *
import game_framework

_images = {}
def load_cached_image(filename):
    if filename in _images:
        return _images[filename]
    image = load_image(filename)
    _images[filename] = image
    return image

class GameObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.size = 0
        self.frame = 0
        self._time = 0
    def init_image(self, clazz, filename, count=1, fps=1):
        clazz.image = load_cached_image(filename)
        clazz._count = count
        clazz._fps = fps
        clazz._width = clazz.image.w // count
        clazz._height = clazz.image.h
        return clazz.image
    def update_frame(self):
        self._time += game_framework.frame_time
        fps = self.fps if hasattr(self, 'fps') else self._fps
        self.frame = round(self._time * fps) % self._count
    def draw(self):
        self.draw_frame()
    def draw_frame(self):
        w, h = self.w, self.h
        if w == 0: w = self.size
        if h == 0: h = self.size

        self.image.clip_draw(self.frame * self._width, 0, self._width, self._height, self.x, self.y, w, h)

