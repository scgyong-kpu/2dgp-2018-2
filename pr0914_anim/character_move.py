from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

frame = 0
x, y = 0, 90
speed = 2

while True:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    x = x + speed
    delay(0.05)
    get_events()

# fill here

close_canvas()
