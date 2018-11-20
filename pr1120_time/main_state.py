from pico2d import *
import game_framework
import game_world
import ui
from player import Player
from missile import Missile

player = None

def enter():
    global player, m1, m2
    # label = ui.Label("Other color", 100, 350, 50, ui.FONT_2)
    # label.color = (255, 127, 127)
    # ui.labels.append(label)
    player = Player()
    m1 = Missile(100, 200, 0, 0, 60)
    m2 = Missile(200, 200, 0, 0, 60)
    print(player)


def draw():
    clear_canvas()
    player.draw()
    m1.draw()
    m2.draw()
    ui.draw()
    update_canvas()

def update():
    ui.update()
    player.update()
    m1.update()
    m2.update()
    delay(0.03)

def handle_events():
    global player
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        player.handle_event(e)
        ui.handle_event(e)

def exit():
    global player
    del(player)
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
