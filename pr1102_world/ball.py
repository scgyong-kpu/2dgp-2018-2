from pico2d import *
import game_world

class Ball:
	image = None
	def __init__(self, x=50, y=300, dx=1, dy=0):
		if (Ball.image == None):
			Ball.image = load_image('../res/ball21x21.png')
		self.x, self.y = x, y
		self.dx, self.dy = dx, dy
	def draw(self):
		self.image.draw(self.x, self.y)
	def update(self):
		self.x += self.dx
		self.y += self.dy