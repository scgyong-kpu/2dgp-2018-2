from pico2d import *
import game_world

DEL_MARGIN = 25

class Ball:
    image = None
    canvas_width = 0
    canvas_height = 0
    def __init__(self, x=50, y=300, dx=1, dy=0):
        if Ball.image == None:
            Ball.image = load_image('../res/ball21x21.png')
        if Ball.canvas_width == 0:
            Ball.canvas_width = get_canvas_width()
            Ball.canvas_height = get_canvas_height()
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.x += self.dx
        self.y += self.dy

        self.dx *= 0.99
        self.dy -= 10 / 30

        if self.x < -DEL_MARGIN or \
         self.x > self.canvas_width + DEL_MARGIN or \
         self.y < -DEL_MARGIN or \
         self.y > self.canvas_height + DEL_MARGIN:
            game_world.remove_object(self)