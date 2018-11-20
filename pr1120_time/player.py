from pico2d import *
import game_framework
import time

class Player:
	image = None
	RUN_SPEED_PPS = 300
	FIELD_MARGIN = 50
	def __init__(self):
		self.field_width, self.field_height = get_canvas_width(), get_canvas_height()
		self.x, self.y = self.field_width / 2, self.field_height / 2
		self.dx, self.dy = 0, 0
		self.speed = 1
		self.size = 60
		self.life = 5
		self.score = 0
		if (Player.image == None):
			Player.image = load_image('player.png')
	def draw(self):
		self.image.draw(self.x, self.y)
	def handle_event(self, event):
		if event.type == SDL_KEYDOWN:
			if event.key == SDLK_LEFT: self.dx += -1
			elif event.key == SDLK_RIGHT: self.dx += 1
			elif event.key == SDLK_UP: self.dy += 1
			elif event.key == SDLK_DOWN: self.dy -= 1

		if event.type == SDL_KEYUP:
			if event.key == SDLK_LEFT: self.dx += 1
			elif event.key == SDLK_RIGHT: self.dx += -1
			elif event.key == SDLK_UP: self.dy -= 1
			elif event.key == SDLK_DOWN: self.dy += 1
	def update(self):
		distance = Player.RUN_SPEED_PPS * game_framework.frame_time 
		self.x += (self.dx * distance)
		self.y += (self.dy * distance)
		self.x = clamp(Player.FIELD_MARGIN, self.x, self.field_width - Player.FIELD_MARGIN) 
		self.y = clamp(Player.FIELD_MARGIN, self.y, self.field_height - Player.FIELD_MARGIN)



