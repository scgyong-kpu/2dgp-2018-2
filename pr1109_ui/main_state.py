from pico2d import *
import game_framework
import ui
from game_session import GameSession

wants = False
score = 0
def addScore(amount):
    global score
    score += amount
    scoreLabel.text = "Score: %05d" % score
    msg = {'amount':amount,'score':score}
    sess.send(msg)

def onOpponentMsg(msg, context):
    print("Mqtt:", msg)
    networkLabel.text = str(msg)
    print(type(msg))
    # opScoreLabel.text = str(score + 100000)
    if 'score' in msg:
        score = msg['score']
        opScoreLabel.text = "Oppon: %05d" % score

def onClick(context):
    global wants
    print("Button click:", context)
    if 'connect' in context:
        wants = not wants
        sess.wantGame(wants)
        networkLabel.text = "Want" if wants else "No thanks"
        return

    if 'score' in context:
        addScore(context['score'])

def enter():
    global scoreLabel
    global networkLabel
    global opScoreLabel
    xs = [200, 400, 600]
    ids = [{'score':100}, {'score':10},{'score':1}]
    for i in range(len(xs)):
        btn = ui.Button('check', xs[i], 500, onClick, ids[i])
        ui.buttons.append(btn)

    btn = ui.Button('check', 700, 100, onClick, {'connect':True})
    ui.buttons.append(btn)

    label = ui.Label("Hello world", 100, 200, 50, ui.FONT_1)
    ui.labels.append(label)
    label = ui.Label("Same font", 100, 250, 50, ui.FONT_1)
    label.color = (0, 127, 0)
    ui.labels.append(label)

    label = ui.Label("Quick brown fox scores 210,000", 100, 100, 20, ui.FONT_2)
    ui.labels.append(label)
    networkLabel = label

    label = ui.Label("Other color", 100, 400, 50, ui.FONT_2)
    label.color = (127, 127, 255)
    ui.labels.append(label)
    scoreLabel = label

    label = ui.Label("Other color", 100, 350, 50, ui.FONT_2)
    label.color = (255, 127, 127)
    ui.labels.append(label)
    opScoreLabel = label
    global sess
    sess = GameSession(onOpponentMsg)

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
    sess.close()

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
