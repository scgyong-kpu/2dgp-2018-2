from pico2d import *
import random
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
    game_world.add_object(player, game_world.layer_player)
    for i in range(10):
        x = random.randint(100, 700)
        y = random.randint(100, 500)
        m = Missile(x, y, 0, 0, 60)
        game_world.add_object(m, game_world.layer_obstacle)
    print(game_world.count_at_layer(game_world.layer_obstacle))

def draw():
    clear_canvas()
    game_world.draw()
    ui.draw()
    update_canvas()

def update():
    ui.update()
    game_world.update()
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
    game_world.clear()

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
