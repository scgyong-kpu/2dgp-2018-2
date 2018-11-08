from pico2d import *
import random
import time
import game_world

class IdleState:
    @staticmethod
    def enter(boy):
        boy.time = time.time()
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def update(boy):
        boy.frame = (boy.frame + 1) % 8
        elapsed = time.time() - boy.time
        if elapsed > 10.0:
            boy.set_state(SleepState)
    @staticmethod
    def draw(boy):
        y = 200 if boy.dir == 0 else 300
        Boy.image.clip_draw(boy.frame * 100, y, 100, 100, *boy.pos())

class RunState:
    MARGIN = 25
    @staticmethod
    def enter(boy):
        boy.time = time.time()
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def update(boy):
        elapsed = time.time() - boy.time
        mag = 2 if elapsed > 2.0 else 1
        # print(mag, elapsed)
        boy.frame = (boy.frame + 1) % 8
        boy.x = boy.x + mag * boy.mag * boy.dx
        boy.y = boy.y + mag * boy.mag * boy.dy
        if hasattr(boy.bg, 'clamp'):
            boy.bg.clamp(boy)

    @staticmethod
    def draw(boy):
        src_y = 0 if boy.dir == 0 else 100
        Boy.image.clip_draw(boy.frame * 100, src_y, 100, 100, *boy.pos())

class SleepState:
    @staticmethod
    def enter(boy):
        boy.time = time.time()
    @staticmethod
    def exit(boy):
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
        x, y = boy.pos()
        Boy.image.clip_composite_draw(boy.frame * 100, y, 100, 100, 
            angle, '', x + mx, y - 25, 100, 100)


class Boy:
    image = None

    def __init__(self):
        print("Creating..")
        self.x = random.randint(0, 200)
        # self.y = random.randint(90, 550)
        self.y = 90
        self.speed = random.uniform(5.0, 8.0)
        self.frame = random.randint(0, 7)
        self.state = None
        self.set_state(IdleState)
        self.dir = 1
        self.dx = 0
        self.dy = 0
        self.mag = 1
        if Boy.image == None:
            Boy.image = load_image('../res/animation_sheet.png')

    def pos(self):
        return self.x - self.bg.x, self.y - self.bg.y

    def draw(self):
        self.state.draw(self)

    def update(self):
        self.state.update(self)

    def handle_event(self, e):
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.dx += self.speed
            if self.dx > 0: self.dir = 1
        elif (e.type, e.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.dx -= self.speed
            if self.dx < 0: self.dir = 0
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.dx -= self.speed
            if self.dx < 0: self.dir = 0
        elif (e.type, e.key) == (SDL_KEYUP, SDLK_LEFT):
            self.dx += self.speed
            if self.dx > 0: self.dir = 1
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_UP):
            self.dy += self.speed
        elif (e.type, e.key) == (SDL_KEYUP, SDLK_UP):
            self.dy -= self.speed
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.dy -= self.speed
        elif (e.type, e.key) == (SDL_KEYUP, SDLK_DOWN):
            self.dy += self.speed
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LSHIFT):
            self.mag = 2.0
        elif (e.type, e.key) == (SDL_KEYUP, SDLK_LSHIFT):
            self.mag = 1.0

        self.set_state(IdleState if self.dx == 0 and self.dy == 0 else RunState)
    def set_state(self, state):
        if self.state == state: return

        if self.state and self.state.exit:
            self.state.exit(self)

        self.state = state

        if self.state.enter:
            self.state.enter(self)
    # def fire_ball(self, big):
    #     mag = 1.5 if self.dir == 1 else -1.5
    #     ballSpeed = mag * self.speed + self.dx

    #     ySpeed = 2 * self.speed * (1 + random.random())
    #     if big: ySpeed *= 0.75
    #     ball = Ball(big, self.x, self.y, ballSpeed, ySpeed)
    #     game_world.add_object(ball, game_world.layer_obstacle)
