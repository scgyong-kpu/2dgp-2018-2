from pico2d import *
import random

class Grass:
	def __init__(self):
		self.image = load_image('../res/grass.png')
		print(self.image)
	def draw(self):
		self.image.draw(400, 30)

class Boy:
    def __init__(self):
        print("Creating..")
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.image = load_image('../res/run_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        if len(waypoints) > 0:
            tx, ty = waypoints[0]
            dx, dy = tx - self.x, ty - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

                if dx < 0 and self.x < tx: self.x = tx
                if dx > 0 and self.x > tx: self.x = tx
                if dy < 0 and self.y < ty: self.y = ty
                if dy > 0 and self.y > ty: self.y = ty

                if (tx, ty) == (self.x, self.y):
                    del waypoints[0]

def handle_events():
    global running
    global waypoints
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT: 
           running = False
        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            running = False
        if e.type == SDL_MOUSEBUTTONDOWN:
            tx, ty = e.x, 600 - e.y
            waypoints += [ (tx, ty) ]


# tx, ty = 800 // 2, 600 // 2
waypoints = []
open_canvas()

g = Grass()
# b = Boy()
# b2 = Boy()
# b2.y = 200

boys = [ Boy() for i in range(20) ]
# boys = []
# for i in range(20):
# 	boys += [ Boy() ]


# for b in boys:
# 	b.y = random.randint(90, 550)

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


