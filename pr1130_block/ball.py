from game_object import *

class Ball(GameObject):
    def __init__(self, x, y, dx, dy):
        super(Ball, self).__init__()
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.size = 22
        self.image = self.init_image(Ball, 'ball.png', 3, 4)
    def update(self):
        self.update_frame()
    def draw(self):
        # print(self.frame, self._count)
        self.draw_frame()
