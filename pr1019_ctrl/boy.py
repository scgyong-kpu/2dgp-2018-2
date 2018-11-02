from pico2d import *
import random
import time

# Boy State
# IDLE, RUN, SLEEP = range(3)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, TIME_OUT = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}

class IdleState:
    @staticmethod
    def enter(boy, event):
        boy.time = time.time()
    @staticmethod
    def exit(boy, event):
        pass
    @staticmethod
    def update(boy):
        boy.frame = (boy.frame + 1) % 8
        elapsed = time.time() - boy.time
        if elapsed > 3.0:
            boy.set_state(SLEEP)
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            y, mx, angle = 300, -25, 3.141592/2
        else:
            y, mx, angle = 200, +25, -3.141592/2
        Boy.image.clip_composite_draw(boy.frame * 100, y, 100, 100, 
            angle, '', boy.x + mx, boy.y - 25, 100, 100)

class RunState:
    @staticmethod
    def enter(boy, event):
        boy.time = time.time()
    @staticmethod
    def exit(boy, event):
        pass
    @staticmethod
    def update(boy):
        elapsed = time.time() - boy.time
        mag = 2 if elapsed > 2.0 else 1
        # print(mag, elapsed)
        boy.frame = (boy.frame + 1) % 8
        boy.x = max(25, min(boy.x + mag * boy.dx, 775))
    @staticmethod
    def draw(boy):
        y = 0 if boy.dir == 0 else 100
        Boy.image.clip_draw(boy.frame * 100, y, 100, 100, boy.x, boy.y)

class SleepState:
    @staticmethod
    def enter(boy, event):
        boy.time = time.time()
    @staticmethod
    def exit(boy, event):
        pass
    @staticmethod
    def update(boy):
        boy.frame = (boy.frame + 1) % 8
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            y, mx, angle = 300, -25, 3.141592/2
        else:
            y, mx, angle = 200, +25, -3.141592/2
        Boy.image.clip_composite_draw(boy.frame * 100, y, 100, 100, 
            angle, '', boy.x + mx, boy.y - 25, 100, 100)

next_state_table = {
    IdleState: { RIGHT_UP: RunState,  LEFT_UP: RunState,  RIGHT_DOWN: RunState,  LEFT_DOWN: RunState, TIME_OUT: SleepState},
    RunState:  { RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState },
    SleepState: { LEFT_DOWN: RunState, RIGHT_DOWN: RunState }
}


class Boy:
    image = None

    def __init__(self):
        print("Creating..")
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(3.0, 5.0)
        self.frame = random.randint(0, 7)
        # self.state = IDLE
        self.state = IdleState
        self.set_state(IdleState)
        self.dir = 1
        self.dx = 0
        if Boy.image == None:
            Boy.image = load_image('../res/animation_sheet.png')

    # def enter_IDLE(self):
    #     self.time = time.time()
    # def draw_IDLE(self):
    #     y = 200 if self.dir == 0 else 300
    #     Boy.image.clip_draw(self.frame * 100, y, 100, 100, self.x, self.y)
    # def update_IDLE(self):
    #     self.frame = (self.frame + 1) % 8
    #     elapsed = time.time() - self.time
    #     if elapsed > 3.0:
    #         self.set_state(SLEEP)

    # def draw_SLEEP(self):
    #     if self.dir == 1:
    #         y, mx, angle = 300, -25, 3.141592/2
    #     else:
    #         y, mx, angle = 200, +25, -3.141592/2
    #     Boy.image.clip_composite_draw(self.frame * 100, y, 100, 100, 
    #         angle, '', self.x + mx, self.y - 25, 100, 100)
    # def update_SLEEP(self):
    #     self.frame = (self.frame + 1) % 8

    # def enter_RUN(self):
    #     self.time = time.time()
    # def draw_RUN(self):
    #     y = 0 if self.dir == 0 else 100
    #     Boy.image.clip_draw(self.frame * 100, y, 100, 100, self.x, self.y)
    # def update_RUN(self):
    #     elapsed = time.time() - self.time
    #     mag = 2 if elapsed > 2.0 else 1
    #     # print(mag, elapsed)
    #     self.frame = (self.frame + 1) % 8
    #     self.x = max(25, min(self.x + mag * self.dx, 775))

    def draw(self):
        self.state.draw(self)

    def update(self):
        self.state.update(self)

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

        if self.state.exit:
            self.state.exit(boy)

        self.state = state

        if self.state.enter:
            self.state.enter(boy)

