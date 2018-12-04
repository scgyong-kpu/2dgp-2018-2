from pico2d import *

class Wall:
    LEFT = 50
    BOTTOM = 50
    TOP = 550
    RIGHT = 450
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
    def didBounce(self, ball):
        ret = False
        if (ball.x < Wall.LEFT or ball.x > Wall.RIGHT):
            ball.angle = math.pi - ball.angle
            ret = True
        if (ball.y < Wall.BOTTOM or ball.y > Wall.TOP):
            ball.angle = -ball.angle
            ret = True
        if ret:
            ball.angle = ball.angle % (2 * math.pi)
            print('angle is now:', ball.angle)
        return ret
