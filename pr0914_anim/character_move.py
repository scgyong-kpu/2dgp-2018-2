from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

frame = 0
x, y = 0, 90
speed = 20
phase = 'right'

while True:
    clear_canvas()
    grass.draw(400, 30)
    if phase == 'right':
        x = x + speed
        if x > 750:
            x = 750
            phase = 'up'
    elif phase == 'up':
        y += speed
        if y >= 550:
            y = 550
            phase = 'left'
    elif phase == 'left':
        x -= speed
        if x < 50:
            x = 50
            phase = 'down'
    elif phase == 'down':
        y -= speed
        if y < 90:
            y = 90
            phase = 'right'

    # print(x, y)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

# fill here

close_canvas()
