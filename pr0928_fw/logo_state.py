from pico2d import *
import game_framework
import boys_state

def enter():
	global logo,count
	count = 0
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
	global count
	if (count > 30):
		game_framework.push_state(boys_state)
		return
	delay(0.03)
	count += 1

def handle_events():
	pass

def pause():
	pass

def resume():
	pass

