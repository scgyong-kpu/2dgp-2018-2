from pico2d import *
import game_framework
import ui

wants = False
score = 0

def enter():
    # label = ui.Label("Other color", 100, 350, 50, ui.FONT_2)
    # label.color = (255, 127, 127)
    # ui.labels.append(label)
    pass

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
