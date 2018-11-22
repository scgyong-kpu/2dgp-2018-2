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
		self.mouse_control = False
		self.angle = 0
		if (Player.image == None):
			Player.image = load_image('player.png')
	def draw(self):
		self.image.draw(self.x, self.y)
	def handle_event(self, event):
		handled = False
		if event.type == SDL_KEYDOWN:
			if event.key in [SDLK_LEFT, SDLK_a]: self.dx += -1
			elif event.key in [SDLK_RIGHT, SDLK_d]: self.dx += 1
			elif event.key in [SDLK_UP, SDLK_w]: self.dy += 1
			elif event.key in [SDLK_DOWN, SDLK_s]: self.dy -= 1

		if event.type == SDL_KEYUP:
			if event.key in [SDLK_LEFT, SDLK_a]: self.dx += 1
			elif event.key in [SDLK_RIGHT, SDLK_d]: self.dx += -1
			elif event.key in [SDLK_UP, SDLK_w]: self.dy -= 1
			elif event.key in [SDLK_DOWN, SDLK_s]: self.dy += 1

		if self.dx != 0 or self.dy != 0:
			self.mouse_control = False
			handled = True

		if event.type == SDL_MOUSEBUTTONDOWN:
			self.mouse_control = True
			handled = True

		if event.type in [SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN]:
			self.mouse_x = event.x
			self.mouse_y = get_canvas_height() - event.y

		return handled

	def update(self):
		distance = Player.RUN_SPEED_PPS * game_framework.frame_time 
		if self.mouse_control:
			mx, my = self.mouse_x - self.x, self.mouse_y - self.y
			angle = math.atan2(mx, my)
			if mx != 0 or my != 0:
				self.angle = int(angle / math.pi * 16) % 32
			dx, dy = math.sin(angle), math.cos(angle)
			tx = self.x + (dx * distance)
			ty = self.y + (dy * distance)
			# print(round(self.x), round(self.y), round(mx, 2), round(my), round(tx), round(ty))
			if dx > 0 and tx > self.mouse_x: tx = self.mouse_x
			if dx < 0 and tx < self.mouse_x: tx = self.mouse_x
			if dy > 0 and ty > self.mouse_y: ty = self.mouse_y
			if dy < 0 and ty < self.mouse_y: ty = self.mouse_y
			self.x, self.y = tx, ty
		else:
			self.x += (self.dx * distance)
			self.y += (self.dy * distance)

		self.x = clamp(Player.FIELD_MARGIN, self.x, self.field_width - Player.FIELD_MARGIN) 
		self.y = clamp(Player.FIELD_MARGIN, self.y, self.field_height - Player.FIELD_MARGIN)



