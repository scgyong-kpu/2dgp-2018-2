from pico2d import *
import game_framework
import game_world
import time

class Player:
	image = None
	RUN_SPEED_PPS = 300
	FIELD_MARGIN = 50
	PADDLE_Y = 100
	def __init__(self):
		self.field_width, self.field_height = get_canvas_width(), get_canvas_height()
		self.size = 60
		self.mouse_control = False
		self.angle = math.pi / 2
		self.init()
		self.life = 0
		self.w = 100
		self.h = 22
		if (Player.image == None):
			Player.image = load_image('paddle.png')
	def init(self, life = 5):
		self.x = self.field_width / 2
		self.y = Player.PADDLE_Y
		self.dx, self.dy = 0, 0
		self.speed = 1
		self.score = 0

	def get_bb(self):
		return self.x - self.w/2, self.y - self.h/2, self.x + self.w/2, self.y + self.h/2

	def didBounce(self, ball):
		if not ball.intersection(self):
			return False
		hw = self.w / 2
		hh = self.h / 2
		if self.x - hw + hh <= ball.x and ball.x <= self.x + hw - hh:
			print('Normal bounce', self.x, ball.x)
			ball.bounceUp()
			return True
		ox = self.x - hw + hh if ball.x < self.x else self.x + hw - hh
		ball.angle = math.atan2(ball.y - self.y, ball.x - ox) % (2 * math.pi)
		return True
	def draw(self):
		# index = int(-(self.angle - math.pi / 2) * 16 / math.pi) % 32
		# self.image.clip_draw(128 * index, 0, 128, 128, self.x, self.y)
		# angle = self.angle - math.pi / 2
		self.image.draw(self.x, self.y)
	def handle_event(self, event):
		handled = False
		if event.type == SDL_KEYDOWN:
			if event.key in [SDLK_LEFT, SDLK_a]: self.dx += -1
			elif event.key in [SDLK_RIGHT, SDLK_d]: self.dx += 1

		if event.type == SDL_KEYUP:
			if event.key in [SDLK_LEFT, SDLK_a]: self.dx += 1
			elif event.key in [SDLK_RIGHT, SDLK_d]: self.dx += -1

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
			# ty = self.y + (dy * distance)
			# print(round(self.x), round(self.y), round(mx, 2), round(my), round(tx), round(ty))
			if dx > 0 and tx > self.mouse_x: tx = self.mouse_x
			if dx < 0 and tx < self.mouse_x: tx = self.mouse_x
			# if dy > 0 and ty > self.mouse_y: ty = self.mouse_y
			# if dy < 0	 and ty < self.mouse_y: ty = self.mouse_y
			self.x = tx
		else:
			self.x += (self.dx * distance)
			# self.y += (self.dy * distance)

		self.x = clamp(Player.FIELD_MARGIN, self.x, self.field_width - Player.FIELD_MARGIN) 
		# self.y = clamp(Player.FIELD_MARGIN, self.y, self.field_height - Player.FIELD_MARGIN)



