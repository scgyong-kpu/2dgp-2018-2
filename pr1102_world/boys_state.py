from pico2d import *
import game_framework
from boy import Boy
import game_world

# from enum import Enum

# BOYS_COUNT = 1000

class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

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
    global boy, grass

    boy = Boy()
    grass = Grass()
    game_world.add_object(grass, game_world.layer_bg)
    game_world.add_object(boy, game_world.layer_player)

def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()

def collides(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > ra: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True
def update():
    game_world.update()
    for ball in game_world.objects_at_layer(game_world.layer_obstacle):
        if collides(boy, ball):
            print("Collision:", ball)
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
