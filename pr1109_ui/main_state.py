from pico2d import *
import game_framework
import ui

def enter():
    for x in [200, 400, 600]:
        btn = ui.Button('check', x, 500)
        ui.buttons.append(btn)

def draw():
    clear_canvas()
    ui.draw()
    update_canvas()

def update():
    ui.update()
    delay(0.03)

def handle_events():
    global boy
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        ui.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
