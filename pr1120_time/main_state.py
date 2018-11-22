from pico2d import *
import random
import game_framework
import game_world
import ui
from player import Player
from missile import Missile
from background import Background

class Life:
    red = None
    white = None
    LIFE_AT_START = 5
    def __init__(self):
        if Life.red == None:
            Life.white = load_image('heart_white.png')
            Life.red = load_image('heart_red.png')
    def draw(self, life):
        x, y = get_canvas_width() - 50, get_canvas_height() - 50
        for i in range(Life.LIFE_AT_START):
            heart = Life.red if i < life else Life.white
            heart.draw(x, y)
            x -= 50

player = None
life = None
scoreLabel = None
gameOverImage = None
GAMESTATE_READY, GAMESTATE_INPLAY, GAMESTATE_PAUSED, GAMESTETE_GAMEOVER = range(4)
gameState = GAMESTATE_READY

def enter():
    global player, life, scoreLabel
    bg = Background()
    game_world.add_object(bg, game_world.layer_bg)
    player = Player()
    game_world.add_object(player, game_world.layer_player)
    life = Life()

    bg.target = player

    label = ui.Label("Score: 0", 35, get_canvas_height() - 55, 45, ui.FONT_2)
    label.color = (255, 127, 127)
    ui.labels.append(label)
    scoreLabel = label

    game_world.isPaused = isPaused

    ready_game()

    global gameOverImage
    gameOverImage = load_image('game_over.png')

def start_game():
    global gameState
    gameState = GAMESTATE_INPLAY
    print("Now state is inplay")

def ready_game():
    global gameState
    gameState = GAMESTATE_READY
    game_world.remove_objects_at_layer(game_world.layer_obstacle)
    player.score = 0
    scoreLabel.text = "Score:  0.0"
    player.life = Life.LIFE_AT_START

def isPaused():
    global gameState
    return gameState != GAMESTATE_INPLAY

def createMissle():
    m = Missile(*gen_random(), random.randint(20, 60))
    game_world.add_object(m, game_world.layer_obstacle)

def collides_distance(a, b):
    dx, dy = a.x - b.x, a.y - b.y
    sq_dist = dx ** 2 + dy ** 2
    radius_sum = a.size / 2 + b.size / 2
    return sq_dist < radius_sum ** 2

def gen_random():
    global player
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

    speed = 1 + player.score / 60
    dx, dy = dx * speed, dy * speed
    return x, y, dx, dy

def draw():
    clear_canvas()
    game_world.draw()
    ui.draw()

    global player
    life.draw(player.life)

    global gameState, gameOverImage
    if gameState == GAMESTETE_GAMEOVER:
        gameOverImage.draw(get_canvas_width() / 2, get_canvas_height() / 2)

    update_canvas()

def update():
    global player, scoreLabel, gameState
    ui.update()
    game_world.update()

    if gameState == GAMESTATE_INPLAY:
        for m in game_world.objects_at_layer(game_world.layer_obstacle):
            collides = collides_distance(player, m)
            if (collides):
                player.life -= 1
                print("Player Life = ", player.life)
                if player.life > 0:
                    game_world.remove_object(m)
                else:
                    gameState = GAMESTETE_GAMEOVER
                break

        player.score += game_framework.frame_time
        str = "Score: {:4.1f}".format(player.score)
        scoreLabel.text = str

    obstacle_count = game_world.count_at_layer(game_world.layer_obstacle)
    # print(obstacle_count)
    if obstacle_count < 10:
        createMissle()
    delay(0.03)
    # print()

def toggle_paused():
    global player, gameState
    if gameState == GAMESTETE_GAMEOVER:
        ready_game()
    elif gameState == GAMESTATE_INPLAY:
        gameState = GAMESTATE_PAUSED
    else:
        gameState = GAMESTATE_INPLAY

def handle_events():
    global player, gameState
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
            toggle_paused()
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if player.mouse_control:
                toggle_paused()
                return

        handled = player.handle_event(e)
        if handled:
            if gameState == GAMESTATE_READY:
                start_game()
            elif gameState == GAMESTATE_PAUSED:
                gameState = GAMESTATE_INPLAY
        ui.handle_event(e)

def exit():
    game_world.clear()

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
