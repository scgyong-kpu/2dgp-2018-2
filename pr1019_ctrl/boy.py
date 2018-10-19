from pico2d import *
import random

class Boy:
    image = None
    wp = None
    RUN_LEFT, RUN_RIGHT, IDLE_LEFT, IDLE_RIGHT = 0, 1, 2, 3
    def __init__(self):
        print("Creating..")
        # self.state = self.State.s1
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.waypoints = []
        self.state = Boy.IDLE_RIGHT
        if Boy.image == None:
            Boy.image = load_image('../res/animation_sheet.png')
        if Boy.wp == None:
            Boy.wp = load_image('../res/wp.png')
    def draw(self):
        for wp in self.waypoints:
            Boy.wp.draw(wp[0], wp[1])
        Boy.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        if len(self.waypoints) > 0:
            tx, ty = self.waypoints[0]
            dx, dy = tx - self.x, ty - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

                if dx < 0 and self.x < tx: self.x = tx
                if dx > 0 and self.x > tx: self.x = tx
                if dy < 0 and self.y < ty: self.y = ty
                if dy > 0 and self.y > ty: self.y = ty

                if (tx, ty) == (self.x, self.y):
                    del self.waypoints[0]
                    self.determine_state()

    def determine_state(self):
        if len(self.waypoints) == 0:
            self.state = Boy.IDLE_RIGHT if self.state == Boy.RUN_RIGHT else  Boy.IDLE_LEFT
        else:
            tx,ty = self.waypoints[0]
            self.state = Boy.RUN_RIGHT if tx > self.x else Boy.RUN_LEFT

    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                tx, ty = e.x, 600 - e.y
                self.waypoints += [ (tx, ty) ]
                self.determine_state()
            else:
                self.waypoints = []
                self.determine_state()
