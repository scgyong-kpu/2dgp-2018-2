from pico2d import *
import game_world
import config

DEL_MARGIN = 25
WIND_RESISTANCE = 0.99#7
BOUNCE_RESISTANCE = 0.70
GRAVITY = 10 / 33
BOUNCING_GROUND = 62

MIN_MOVE = 2

class Ball:
    image = None
    image2 = None
    canvas_width = 0
    canvas_height = 0
    def __init__(self, big, x=50, y=300, dx=1, dy=0):
        if Ball.image == None:
            Ball.image = load_image('../res/ball21x21.png')
            Ball.image2 = load_image('../res/ball41x41.png')
        if Ball.canvas_width == 0:
            Ball.canvas_width = get_canvas_width()
            Ball.canvas_height = get_canvas_height()
        self.big = big
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.stopTimer = 0
    def get_bb(self):
        if self.big:
            return self.x - 20, self.y - 20, self.x + 20, self.y + 20
        else:
            return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    def draw(self):
        if self.big:
            self.image2.draw(self.x, self.y)
        else:
            self.image.draw(self.x, self.y)
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())
    def update(self):
        if self.stopTimer > 0:
            elapsed = get_time() - self.stopTimer
            if elapsed > 3.0:
                game_world.remove_object(self)
            return

        self.x += self.dx
        self.y += self.dy

        self.dx *= WIND_RESISTANCE
        self.dy -= GRAVITY

        height = self.y - BOUNCING_GROUND
        if height < 0:
            self.y -= height
            self.dy *= -BOUNCE_RESISTANCE

        if math.fabs(height) < MIN_MOVE and \
         math.fabs(self.dx) < MIN_MOVE and \
         math.fabs(self.dy) < MIN_MOVE:
            self.dx = self.dy = 0
            self.y = BOUNCING_GROUND
            self.stopTimer = get_time()

        if self.x < -DEL_MARGIN or \
         self.x > self.canvas_width + DEL_MARGIN or \
         self.y < -DEL_MARGIN or \
         self.y > self.canvas_height + DEL_MARGIN:
            game_world.remove_object(self)