from pico2d import *
import random
import game_framework
import game_world

class Item(object):
    image = None
    RUN_SPEED_PPS = 200
    def __init__(self, x, y, dx, dy):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.size = 48
        self.score = 7.5
        if (Item.image == None):
            Item.image = load_image('present_box.png')

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def update(self):
        if game_world.isPaused(): return
        self.x += Item.RUN_SPEED_PPS * game_framework.frame_time * self.dx
        self.y += Item.RUN_SPEED_PPS * game_framework.frame_time * self.dy     
        if self.x < -self.size or  \
         self.y < -self.size or \
         self.x > get_canvas_width() + self.size or \
         self.y > get_canvas_height() + self.size:
            game_world.remove_object(self)

