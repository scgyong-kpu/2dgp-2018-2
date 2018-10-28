from pico2d import *
import random
import time


class Player:
    bodyImage = None
    barrelImage = None
    interested_keys = [ SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN ]

    def __init__(self):
        self.x = 400
        self.y = 300
        self.angle = 0
        self.moveSpeed = 10
        self.rotSpeed = 10
        self.keys = {}
        for k in Player.interested_keys: self.keys[k] = False
        if Player.bodyImage == None:
            Player.bodyImage = load_image('player_body_pix.png')
        if Player.barrelImage == None:
            Player.barrelImage = load_image('player_barrel_pix.png')

    def draw(self):
        self.bodyImage.draw(self.x, self.y)
        self.barrelImage.draw(self.x, self.y)

    def update(self):
        mag   = -1 if self.keys[SDLK_LEFT] else 0
        mag  +=  1 if self.keys[SDLK_RIGHT] else 0
        move  =  1 if self.keys[SDLK_UP] else 0
        move += -1 if self.keys[SDLK_DOWN] else 0
        print(mag, move)

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN or e.type == SDL_KEYUP:
            if e.key in Player.interested_keys:
                self.keys[e.key] = e.type == SDL_KEYDOWN
                print(e.key, e.type == SDL_KEYDOWN)
        pass

