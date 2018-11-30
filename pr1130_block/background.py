from pico2d import *

class Background:
    image_space = None
    image_stars = None
    def __init__(self):
        # if (Background.image_space == None):
        #     Background.image_space = load_image('outerspace.png')
        #     Background.image_stars = load_image('stars.png')
        self.space_point = 0, 0
        self.stars_point = 0, 0
        self.target = None
    def draw(self):
        pass
        # Background.image_space.draw(*self.space_point)
        # Background.image_stars.draw(*self.stars_point)
    def update(self):
        pass
        # hw = get_canvas_width() / 2
        # hh = get_canvas_height() / 2
        # dx, dy = (self.target.x - hw), (self.target.y - hh)
        # self.space_point = hw - 0.02 * dx, hh - 0.02 * dy
        # self.stars_point = hw - 0.05 * dx, hh - 0.05 * dy

