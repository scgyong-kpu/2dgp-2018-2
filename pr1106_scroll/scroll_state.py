from pico2d import *
import game_framework
from boy import Boy
import game_world
from tilebg import TiledBackground as Background

# from enum import Enum

# BOYS_COUNT = 1000

def handle_events():
    global boy
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        else:
            boy.handle_event(e)

def enter():
    global boy

    boy = Boy()
    bg = Background()

    boy.bg = bg
    bg.target = boy

    game_world.add_object(bg, game_world.layer_bg)
    game_world.add_object(boy, game_world.layer_player)

def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()

def update():
    game_world.update()
    delay(0.03)

# fill here

def exit():
    game_world.clear()

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
