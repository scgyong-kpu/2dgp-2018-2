from pico2d import *

class Button:
    def __init__(self, normal, selected, x, y):
        self.normalImage = load_image(normal)
        self.selectedImage = load_image(selected)
        self.x, self.y = x, y
        self.selected = False
    def draw(self):
        if self.selected:
            self.selectedImage.draw(self.x, self.y)
        else:
            self.normalImage.draw(self.x, self.y)
    def hits(self, x, y):
        hw, hh = self.normalImage.w // 2, self.normalImage.h // 2
        if x < self.x - hw: return False
        if x > self.x + hw: return False
        if y < self.y - hh: return False
        if y > self.y + hw: return False
        return True
