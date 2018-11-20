from pico2d import *

class Background:
    image_space = None
    image_stars = None
    def __init__(self):
        if (Background.image_space == None):
            Background.image_space = load_image('outerspace.png')
            Background.image_stars = load_image('stars.png')
    def draw(self):
        Background.image_space.draw(400, 300)
        Background.image_stars.draw(400, 300)
    def update(self):
        pass

