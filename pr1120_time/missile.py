from pico2d import *
import random
import game_framework
import game_world
from game_object import GameObject

class Missile(GameObject):
    # image = None
    RUN_SPEED_PPS = 200
    def __init__(self, x, y, dx, dy, size):
        super(Missile, self).__init__()
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.size = size
        self.w = 2 * size
        self.h = 2 * size
        self.fps = 8 + random.randint(0, 20)
        self.frame = random.randint(0, 23)
        self.init_image(Missile, 'fireball.png', 24)

    # def draw(self):
    # 	self.image.clip_draw(128 * self.frame, 0, 128, 128, self.x, self.y, 2 * self.size, 2 * self.size)

    def update(self):
        super(Missile,self).update_frame()
        if game_world.isPaused():
            return
        self.x += Missile.RUN_SPEED_PPS * game_framework.frame_time * self.dx
        self.y += Missile.RUN_SPEED_PPS * game_framework.frame_time * self.dy
        if self.x < -self.size or  \
         self.y < -self.size or \
         self.x > get_canvas_width() + self.size or \
         self.y > get_canvas_height() + self.size:
            game_world.remove_object(self)

    def isInField(self, width, height):
        if (self.x < 0): return False
        if (self.y < 0): return False
        if (self.x > width): return False
        if (self.y > height): return False
        return True