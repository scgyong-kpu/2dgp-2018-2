from pico2d import *

speed = 10

def handle_events():
    global running
    global x, y
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
            x, y = e.x, 600 - e.y

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

x, y = 800 // 2, 90
frame = 0
running = True
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.01)

# fill here
    
close_canvas()
