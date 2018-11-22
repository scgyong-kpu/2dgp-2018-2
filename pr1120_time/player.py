from pico2d import *
import game_framework
import game_world
import time

class Player:
	image = None
	RUN_SPEED_PPS = 300
	FIELD_MARGIN = 50
	def __init__(self):
		self.field_width, self.field_height = get_canvas_width(), get_canvas_height()
		self.size = 60
		self.mouse_control = False
		self.angle = math.pi / 2
		self.init()
		if (Player.image == None):
			Player.image = load_image('BattleCruiser.png')
	def init(self, life = 5):
		self.x, self.y = self.field_width / 2, self.field_height / 2
		self.dx, self.dy = 0, 0
		self.speed = 1
		self.life = life
		self.score = 0

	def draw(self):
		index = int(-(self.angle - math.pi / 2) * 16 / math.pi) % 32
		self.image.clip_draw(128 * index, 0, 128, 128, self.x, self.y)
		# angle = self.angle - math.pi / 2
		# self.image.clip_composite_draw(0, 0, 128, 128, angle, '', self.x, self.y, 128, 128)
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
		if game_world.isPaused():
			return
		distance = Player.RUN_SPEED_PPS * game_framework.frame_time 
		if self.mouse_control:
			mx, my = self.mouse_x - self.x, self.mouse_y - self.y
			angle = math.atan2(my, mx)
			if mx != 0 or my != 0:
				self.angle = angle
			dx, dy = math.cos(angle), math.sin(angle)
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



