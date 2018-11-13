from pico2d import *
import game_framework
import ui

def onClick(context):
    print("Button click:", context)

def enter():
    xs = [200, 400, 600]
    ids = ['hello', 32, { 'hello':'world', 'key':12.3}]
    for i in range(len(xs)):
        btn = ui.Button('check', xs[i], 500, onClick, ids[i])
        ui.buttons.append(btn)
    label = ui.Label("Hello world", 100, 200, 50, ui.FONT_1)
    ui.labels.append(label)
    label = ui.Label("Same font", 100, 250, 50, ui.FONT_1)
    label.color = (0, 127, 0)
    ui.labels.append(label)
    label = ui.Label("Quick brown fox scores 210,000", 100, 100, 20, ui.FONT_2)
    ui.labels.append(label)
    label = ui.Label("Other color", 100, 50, 50, ui.FONT_2)
    label.color = (127, 127, 255)
    ui.labels.append(label)

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
