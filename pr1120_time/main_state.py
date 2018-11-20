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
        createMissle()
    print(game_world.count_at_layer(game_world.layer_obstacle))

def createMissle():
    m = Missile(*gen_random(), 60)
    game_world.add_object(m, game_world.layer_obstacle)

score = 0

def gen_random():
    global score
    field_width = get_canvas_width()
    field_height = get_canvas_height()
    dx, dy = random.random(), random.random()
    if (dx < 0.5): dx -= 1
    if (dy < 0.5): dy -= 1

    side = random.randint(1, 4) # 1=top, 2=left, 3=bottom, 4=right
    if (side == 1): # top
        x, y = random.randint(0, field_width), 0
        if (dy < 0): dy = -dy

    if (side == 2): # left
        x, y = 0, random.randint(0, field_height)
        if (dx < 0): dx = -dx

    if (side == 3): # bottom
        x, y = random.randint(0, field_width), field_height
        if (dy > 0): dy = -dy

    if (side == 4): # right
        x, y = field_width, random.randint(0, field_height)
        if (dx > 0): dx = -dx

    speed = 1 + score / 60
    dx, dy = dx * speed, dy * speed
    return x, y, dx, dy

def draw():
    clear_canvas()
    game_world.draw()
    ui.draw()
    update_canvas()

def update():
    ui.update()
    game_world.update()
    obstacle_count = game_world.count_at_layer(game_world.layer_obstacle)
    print(obstacle_count)
    if obstacle_count < 10:
        createMissle()
    delay(0.03)
    print()

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
