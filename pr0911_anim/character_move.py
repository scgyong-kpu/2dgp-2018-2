from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

frame = 0
x = 0
while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    frame = frame + 1
    if (frame >= 8): frame = 0
    update_canvas()
    x = x + 2
    delay(0.05)

# fill here

close_canvas()
