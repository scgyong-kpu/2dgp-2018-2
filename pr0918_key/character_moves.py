from pico2d import *

speed = 2

def handle_events():
    global running
    global x
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                x -= speed
            elif e.key == SDLK_RIGHT:
                x += speed

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
running = True
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()
    handle_events()
    delay(0.01)

# fill here
    
close_canvas()
