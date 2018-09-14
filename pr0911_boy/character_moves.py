from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (x < 800):
	clear_canvas()
	grass.draw(400, 30)
	character.draw(x, 90)
	update_canvas()
	x = x + 2
	delay(0.01)

# fill here
    
close_canvas()
