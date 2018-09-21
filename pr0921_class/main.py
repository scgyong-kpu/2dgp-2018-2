from pico2d import *
import random

class Grass:
	def __init__(self):
		self.image = load_image('../res/grass.png')
		print(self.image)
	def draw(self):
		self.image.draw(400, 300)

class Boy:
	def __init__(self):
		print("Creating..")
		self.x, self.y = 0, 90
		self.frame = 0
		self.image = load_image('../res/run_animation.png')
	def draw(self):
		self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.frame = (self.frame + 1) % 8
		self.x += 2

def handle_events():
	global running
	events = get_events()
	for e in events:
		if e.type == SDL_QUIT: 
			running = False
		if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
			running = False

open_canvas()

g = Grass()
# b = Boy()
# b2 = Boy()
# b2.y = 200
boys = [ Boy() ] * 20
for b in boys:
	b.y = random.randint(90, 550)

running = True


while running:
	handle_events()

	for b in boys:
		b.update()
	# b.update()
	# b2.update()

	clear_canvas()
	g.draw()
	for b in boys:
		b.draw()
	# b.draw()
	# b2.draw()
	update_canvas()

	delay(0.03)


