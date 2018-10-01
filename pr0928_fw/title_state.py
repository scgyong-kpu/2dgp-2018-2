from pico2d import *
import game_framework
import boys_state

def enter():
	global bgImage
	bgImage = load_image('../res/title.png')

def exit():
	global bgImage
	del bgImage

def draw():
	clear_canvas()
	bgImage.draw(400, 300)
	update_canvas()

def update():
	delay(0.03)

def handle_events():
	events = get_events()
	for e in events:
		if e.type == SDL_QUIT:
			game_framework.quit()
		elif e.type == SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				game_framework.quit()
				# game_framework.pop_state()
			elif e.key == SDLK_SPACE:
				game_framework.push_state(boys_state)

def pause():
	pass

def resume():
	pass

