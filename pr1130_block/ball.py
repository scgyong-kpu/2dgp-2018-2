import game_framework
from game_object import *

class Ball(GameObject):
    PPS = 100
    def __init__(self, x, y, dx, dy):
        super(Ball, self).__init__()
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.size = 22
        self.w, self.h = 22, 22
        self.angle = 1.0
        self.speed = 3.0
        self.image = self.init_image(Ball, 'ball.png', 3, 4)
    def update(self):
        self.update_frame()
        distance = game_framework.frame_time * Ball.PPS * self.speed
        dx = distance * math.cos(self.angle)
        dy = distance * math.sin(self.angle)
        self.x += dx
        self.y += dy
    def draw(self):
        # print(self.frame, self._count)
        self.draw_frame()
