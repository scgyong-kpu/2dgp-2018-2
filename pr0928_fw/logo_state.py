from pico2d import *
import game_framework

def enter():
	global logo
	open_canvas()
	logo = load_image('../res/kpu_credit.png')

def exit():
	del logo
	#logo = None

def draw():
	clear_canvas()
	logo.draw(400, 300)
	update_canvas()

def update():
	delay(0.03)

def handle_events():
	pass

def pause():
	pass

def resume():
	pass

