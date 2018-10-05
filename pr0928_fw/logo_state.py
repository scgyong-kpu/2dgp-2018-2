from pico2d import *
import game_framework
# import boys_state
import title_state
import time

def enter():
	global logo,startedOn
	startedOn = time.time()
	logo = load_image('../res/kpu_credit.png')

def exit():
	global logo
	del logo
	#logo = None

def draw():
	clear_canvas()
	logo.draw(400, 300)
	update_canvas()

def update():
	global startedOn
	elapsed = time.time() - startedOn
	print(elapsed)
	if elapsed >= 1.0:
		game_framework.change_state(title_state)
		return
	delay(0.03)

def handle_events():
	pass

def pause():
	pass

def resume():
	pass

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()

