from pico2d import *
import random
import game_framework
import game_world
import ui
import json
from player import Player
from ball import Ball
from background import Background
from highscore import Highscore
from wall import Wall
from brick import Brick
from game_object import GameObject

GAMESTATE_READY, GAMESTATE_INPLAY, GAMESTATE_PAUSED, GAMESTETE_GAMEOVER = range(4)
BULLETS_AT_START = 10
NUM_KEYS = [ \
    SDLK_0, SDLK_1, SDLK_2, SDLK_3, SDLK_4, \
    SDLK_5, SDLK_6, SDLK_7, SDLK_8, SDLK_9 \
]

class Life:
    red = None
    white = None
    LIFE_AT_START = 5
    def __init__(self):
        pass
        # if Life.red == None:
        #     Life.white = load_image('heart_white.png')
        #     Life.red = load_image('heart_red.png')
    def draw(self, life):
        pass
        # x, y = get_canvas_width() - 50, get_canvas_height() - 50
        # for i in range(Life.LIFE_AT_START):
        #     heart = Life.red if i < life else Life.white
        #     heart.draw(x, y)
        #     x -= 50


player = None
ball = None
wall = None
# bricks
life = None
scoreLabel = None
highscore = None
gameOverImage = None
music_bg = None
wav_bomb = None
wav_item = None
gameState = GAMESTATE_READY
stage = None
saved = True
max_stage_number = 1
brick = None

def enter():
    global player, life, scoreStatic, scoreLabel
    bg = Background()
    game_world.add_object(bg, game_world.layer_bg)
    player = Player()
    game_world.add_object(player, game_world.layer_player)
    life = Life()

    global ball
    ball = Ball(400, 400, 1, 1)
    game_world.add_object(ball, game_world.layer_player)

    global wall
    wall = Wall()
    game_world.add_object(wall, game_world.layer_bg)
    bg.target = player

    global stage_number
    stage_number = 1

    cw = get_canvas_width()
    ch = get_canvas_height()

    label = ui.Label("Score:", cw - 200, ch - 55, 36, ui.FONT_2)
    label.color = (255, 191, 127)
    ui.labels.append(label)
    scoreStatic = label

    label = ui.Label("0", cw - 200, ch - 100, 36, ui.FONT_2)
    label.color = (255, 191, 127)
    ui.labels.append(label)
    scoreLabel = label

    global stageStatic, stageLabel
    label = ui.Label("Stage:", cw - 200, ch - 155, 36, ui.FONT_2)
    label.color = (255, 191, 127)
    ui.labels.append(label)
    stageStatic = label

    label = ui.Label("1", cw - 200, ch - 200, 36, ui.FONT_2)
    label.color = (255, 191, 127)
    ui.labels.append(label)
    stageLabel = label

    global bgStatic, bgLabel
    label = ui.Label("BG Idx:", cw - 200, ch - 255, 36, ui.FONT_2)
    label.color = (255, 191, 127)
    ui.labels.append(label)
    bgStatic = label

    label = ui.Label("1", cw - 200, ch - 300, 36, ui.FONT_2)
    label.color = (255, 191, 127)
    ui.labels.append(label)
    bgLabel = label

    global highscore
    highscore = Highscore()

    global music_bg, wav_bomb, wav_item
    # music_bg = load_music('background.mp3')
    # wav_bomb = load_wav('explosion.wav')
    # wav_item = load_wav('item.wav')

    game_world.isPaused = isPaused

    ready_game()

    global gameOverImage
    # gameOverImage = load_image('game_over.png')

def start_game():
    global gameState
    gameState = GAMESTATE_INPLAY

    global music_bg
    # music_bg.set_volume(64)
    # music_bg.repeat_play()

def goto_next_stage():
    global stage_number, max_stage_number, saved
    if not saved:
        return
    if stage_number >= max_stage_number: return
    stage_number += 1
    ready_game()

def goto_prev_stage():
    global stage_number, saved
    if not saved:
        return
    if stage_number == 1: return
    stage_number -= 1
    ready_game()

def ready_game():
    global gameState
    gameState = GAMESTATE_READY
    game_world.remove_objects_at_layer(game_world.layer_obstacle)
    game_world.remove_objects_at_layer(game_world.layer_item)

    global stage_number, max_stage_number

    try:
        f = open('stage_' + str(stage_number) + '.json', 'r')
        data = json.load(f)
        f.close()
        if max_stage_number <= stage_number:
            max_stage_number = stage_number + 1
    except IOError:
        data = None

    global stage

    if data == None:
        bricks = []
        stage['bricks'] = []
    else:
        stage = data

        wall.bg_index = data['bg_pattern']
        bricks = data['bricks']

    global ball
    ball.x, ball.y, ball.angle, ball.speed = tuple(stage['ball'])
    for d in bricks:
        b = Brick(d["x"], d["y"], d["t"])
        game_world.add_object(b, game_world.layer_obstacle)

    global scoreStatic, scoreLabel
    if 'label_s1' in stage:
        scoreStatic.color = tuple(stage['label_s1'])
    if 'label_s2' in stage:
        scoreLabel.color = tuple(stage['label_s2'])
    # player.init(Life.LIFE_AT_START)

    global brick
    brick = Brick(0, 0, 1, True)

    update_score()
    update_stage_label()
    update_bg_index()

def update_stage_label():
    global stageLabel, saved
    stageLabel.text = str(stage_number)
    if not saved:
        stageLabel.text += ' Edit'

def update_bg_index():
    global bgLabel, wall, stage
    bgLabel.text = str(wall.bg_index)
    stage['bg_pattern'] = wall.bg_index

def save():
    global stage, saved, stage_number, max_stage_number
    bricks = list(game_world.objects_at_layer(game_world.layer_obstacle))
    stage['bricks'] = list(map(Brick.dict, bricks))
    print(stage)
    f = open('stage_' + str(stage_number) + '.json', 'w')
    json.dump(stage, f, indent = 2)
    f.close()
    saved = True
    if max_stage_number <= stage_number:
        max_stage_number = stage_number + 1

    update_stage_label()

def mark_edited():
    global saved
    saved = False
    update_stage_label()

def add_brick(x, y):
    global saved, brick
    for b in game_world.objects_at_layer(game_world.layer_obstacle):
        if GameObject.intersection(b, brick) != None:
            game_world.remove_object(b)
            return
    game_world.add_object(brick, game_world.layer_obstacle)
    mark_edited()
    brick = Brick(x, y, brick.type, True)

def move_brick(x, y):
    global brick
    x, y = x // 11 * 11 - 7, y // 11 * 11 + 5
    brick.x, brick.y = x, y
 
def end_game():
    global gameState, player, highscore
    gameState = GAMESTETE_GAMEOVER
    highscore.add(Highscore.Entry(player.score))

    global music_bg
    music_bg.stop()

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

    global brick
    brick.draw()

    global player
    life.draw(player.life)

    global wall
    wall.drawRight()

    # global gameState, gameOverImage
    # if gameState == GAMESTETE_GAMEOVER:
    #     gameOverImage.draw(get_canvas_width() / 2, get_canvas_height() / 2)
    #     highscore.draw()

    update_canvas()

def update():
    global player, gameState, wav_bomb, wav_item

    if gameState != GAMESTATE_INPLAY:
        delay(0.01)
        return

    ui.update()
    game_world.update()
    global wall, ball
    wall.didBounce(ball)
    player.didBounce(ball)

    global stage, stage_number
    for b in game_world.objects_at_layer(game_world.layer_obstacle):
        if b.didBounce(ball):
            if stage != None and 'scores' in stage:
                score = stage['scores'][b.type]
                # print(b.type, score)
            else:
                score = b.score
            if b.life == 0:
                player.score += score
                update_score()
                count = game_world.count_at_layer(game_world.layer_obstacle)
                if count == 0:
                    goto_next_stage()
            break

    delay(0.01)
    # print()

def update_score():
    global player, scoreLabel
    str = "{:5.0f}".format(player.score)
    scoreLabel.text = str

def toggle_paused():
    global player, gameState
    if gameState == GAMESTETE_GAMEOVER:
        ready_game()
    elif gameState == GAMESTATE_INPLAY:
        gameState = GAMESTATE_PAUSED
        player.score -= 2.0
        if player.score < 0:
            player.score = 0
        update_score()
    else:
        gameState = GAMESTATE_INPLAY

def handle_events():
    global player, gameState, ball, wall, saved, brick
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
            toggle_paused()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFTBRACKET):
            goto_prev_stage()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RIGHTBRACKET):
            goto_next_stage()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_MINUS):
            wall.changeIndex(-1)
            update_bg_index()
            mark_edited()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_EQUALS):
            wall.changeIndex(1)
            update_bg_index()
            mark_edited()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_s):
            save()
        elif e.type == SDL_MOUSEBUTTONDOWN:
            add_brick(e.x, get_canvas_height() - e.y)
        elif e.type == SDL_MOUSEMOTION:
            move_brick(e.x, get_canvas_height() - e.y)
        elif e.type == SDL_KEYDOWN and e.key in NUM_KEYS:
            t = e.key - SDLK_0
            if t == 0: t = 10
            brick.type = t


        # handled = player.handle_event(e)
        # if handled:
        #     if gameState == GAMESTATE_READY:
        #         start_game()
        #     elif gameState == GAMESTATE_PAUSED:
        #         gameState = GAMESTATE_INPLAY
        ui.handle_event(e)

def exit():
    game_world.clear()
    global music_bg, wav_bomb, wav_item
    # del(music_bg)
    # del(wav_bomb)
    # del(wav_item)

    global life, highscore
    del(life)
    del(highscore)

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
