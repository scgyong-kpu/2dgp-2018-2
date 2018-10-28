from pico2d import *
import random
import time


class Player:
    bodyImage = None
    barrelImage = None

    def __init__(self):
        self.x = 400
        self.y = 300
        self.angle = 0
        self.moveSpeed = 10
        self.rotSpeed = 10
        if Player.bodyImage == None:
            Player.bodyImage = load_image('player_body_pix.png')
        if Player.barrelImage == None:
            Player.barrelImage = load_image('player_barrel_pix.png')

    def draw(self):
        self.bodyImage.draw(self.x, self.y)
        self.barrelImage.draw(self.x, self.y)

    def update(self):
        pass

    def handle_event(self, e):
        pass

