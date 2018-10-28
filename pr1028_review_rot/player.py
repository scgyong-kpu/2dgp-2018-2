from pico2d import *
import math


class Player:
    bodyImage = None
    barrelImage = None
    interested_keys = [ SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN ]
    d1, d2 = 16, 35

    def __init__(self):
        self.x = 400
        self.y = 300
        self.angle = 0
        self.bAngle = 0
        self.bx = self.x
        self.by = self.y - Player.d1 + Player.d2
        self.mx = self.x
        self.my = 0
        self.moveSpeed = 100 * 1 / 30
        self.rotSpeed = 1 * math.pi / 60
        self.keys = {}
        for k in Player.interested_keys: self.keys[k] = False
        if Player.bodyImage == None:
            Player.bodyImage = load_image('player_body_pix.png')
        if Player.barrelImage == None:
            Player.barrelImage = load_image('player_barrel_pix.png')

    def draw(self):
        self.bodyImage.composite_draw(self.angle, "", self.x, self.y)
        self.barrelImage.composite_draw(self.angle + self.bAngle, "", self.bx, self.by)

    def update(self):
        mag   =  1 if self.keys[SDLK_LEFT] else 0
        mag  += -1 if self.keys[SDLK_RIGHT] else 0
        move  =  1 if self.keys[SDLK_UP] else 0
        move += -1 if self.keys[SDLK_DOWN] else 0

        # print(mag, move)

        if mag != 0:
            # if move == 0:
            #     self.bAngle += mag * self.rotSpeed
            # else:
                if move < 0: mag = -mag
                self.angle += mag * self.rotSpeed
                # print(mag, self.angle)

        if move != 0:
            self.x += -move * self.moveSpeed * math.sin(self.angle)
            self.y += +move * self.moveSpeed * math.cos(self.angle)

        angle = math.atan2(self.x - self.mx, self.my - self.y)
        self.bAngle = angle - self.angle

        # if mag != 0 or move != 0:
        x, y = self.x, self.y
        x += +Player.d1 * math.sin(self.angle)
        y += -Player.d1 * math.cos(self.angle)
        x += -Player.d2 * math.sin(self.angle + self.bAngle)
        y += +Player.d2 * math.cos(self.angle + self.bAngle)
        self.bx, self.by = x, y

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN or e.type == SDL_KEYUP:
            if e.key in Player.interested_keys:
                self.keys[e.key] = e.type == SDL_KEYDOWN
                # print(e.key, e.type == SDL_KEYDOWN)
        elif e.type == SDL_MOUSEMOTION:
            self.mx, self.my = e.x, 600 - e.y
        pass

