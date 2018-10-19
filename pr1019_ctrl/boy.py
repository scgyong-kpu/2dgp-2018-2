from pico2d import *
import random
import time

# Boy State
IDLE, RUN = range(2)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}

next_state_table = {
    IDLE: { RIGHT_UP: RUN,  LEFT_UP: RUN,  RIGHT_DOWN: RUN,  LEFT_DOWN: RUN  },
    RUN:  { RIGHT_UP: IDLE, LEFT_UP: IDLE, RIGHT_DOWN: IDLE, LEFT_DOWN: IDLE }
}
class Boy:
    image = None

    RUN_LEFT, RUN_RIGHT, IDLE_LEFT, IDLE_RIGHT = 0, 1, 2, 3
    def __init__(self):
        print("Creating..")
        # self.state = self.State.s1
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(3.0, 5.0)
        self.frame = random.randint(0, 7)
        # self.state = IDLE
        self.state = -1
        self.set_state(IDLE)
        self.dir = 1
        self.dx = 0
        if Boy.image == None:
            Boy.image = load_image('../res/animation_sheet.png')

    def draw_IDLE(self):
        y = 200 if self.dir == 0 else 300
        Boy.image.clip_draw(self.frame * 100, y, 100, 100, self.x, self.y)
    def update_IDLE(self):
        self.frame = (self.frame + 1) % 8

    def enter_RUN(self):
        self.time = time.time()
    def draw_RUN(self):
        y = 0 if self.dir == 0 else 100
        Boy.image.clip_draw(self.frame * 100, y, 100, 100, self.x, self.y)
    def update_RUN(self):
        elapsed = time.time() - self.time
        mag = 2 if elapsed > 2.0 else 1
        # print(mag, elapsed)
        self.frame = (self.frame + 1) % 8
        self.x = max(25, min(self.x + mag * self.dx, 775))

    def draw(self):
        self.draw_func(self)
        # if self.state == IDLE:
        #     self.draw_IDLE()
        # elif self.state == RUN:
        #     self.draw_RUN()

    def update(self):
        self.update_func(self)
        # if self.state == IDLE:
        #     self.update_IDLE()
        # elif self.state == RUN:
        #     self.update_RUN()

    def handle_event(self, e):
        if (e.type, e.key) in key_event_table:
            key_event = key_event_table[(e.type, e.key)]
            if key_event == RIGHT_DOWN:
                self.dx += self.speed
                if self.dx > 0: self.dir = 1
            elif key_event == LEFT_DOWN:
                self.dx -= self.speed
                if self.dx < 0: self.dir = 0
            elif key_event == RIGHT_UP:
                self.dx -= self.speed
                if self.dx < 0: self.dir = 0
            elif key_event == LEFT_UP:
                self.dx += self.speed
                if self.dx > 0: self.dir = 1

            self.set_state(IDLE if self.dx == 0 else RUN)
            # print(self.dx, self.dir)
    def set_state(self, state):
        if self.state == state: return

        # print(self.state, Boy.functions[self.state])
        if self.state in Boy.functions:
            exit = Boy.functions[self.state].get('exit', None)
            if (exit):
                exit(self)

        self.state = state

        funcs = Boy.functions[self.state]
        enter = funcs.get('enter', None)
        if enter: enter(self)

        self.draw_func = funcs['draw']
        self.update_func = funcs['update']

    functions = {
        IDLE: {
            'update': update_IDLE,
            'draw': draw_IDLE
        },
        RUN: {
            'enter': enter_RUN,
            'update': update_RUN,
            'draw': draw_RUN
        }
    }

