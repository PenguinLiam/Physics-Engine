
# Game Items File #

import pygame as py

class player(py.sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()
        self.size = size
        self.pos = pos

    def update(self):
        pass


