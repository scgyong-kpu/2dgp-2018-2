from pico2d import *
import game_framework

def enter():
	logo = load_image('../res/kpu_credit.png')

def exit():
	del logo
	#logo = None

def draw():
	logo.draw(400, 300)

def update():
	pass

def handle_events():
	pass

def pause():
	pass

def resume():
	pass

