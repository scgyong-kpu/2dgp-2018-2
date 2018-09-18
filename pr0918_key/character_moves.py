from pico2d import *

speed = 10

def handle_events():
    global running
    global x, dir
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                dir = -1
            elif e.key == SDLK_RIGHT:
                dir = 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                dir = 0
            elif e.key == SDLK_RIGHT:
                dir = 0

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 800 // 2
dir = 0
running = True
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()
    handle_events()
    x += dir
    delay(0.01)

# fill here
    
close_canvas()
