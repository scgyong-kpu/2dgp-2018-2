from pico2d import *
import random
import game_framework

class Missile:
	image = None
	RUN_SPEED_PPS = 200
	def __init__(self, x, y, dx, dy, size):
		self.x, self.y = x, y
		self.dx, self.dy = dx, dy
		self.size = size
		if (Missile.image == None):
			Missile.image = load_image('missile.png')

	def draw(self):
		self.image.draw(self.x, self.y, self.size, self.size)

	def update(self):
		self.x += Missile.RUN_SPEED_PPS * game_framework.frame_time * self.dx
		self.y += Missile.RUN_SPEED_PPS * game_framework.frame_time * self.dy		

	def isInField(self, width, height):
		if (self.x < 0): return False
		if (self.y < 0): return False
		if (self.x > width): return False
		if (self.y > height): return False
		return True