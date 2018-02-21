
# =========================================================================== #
''' Game Items File '''
# =========================================================================== #

import Variables as v
import pygame as py



# Temp player class using a rect to define a player
class player(py.sprite.Sprite):
    def __init__(self, size, pos, colour=v.black):
        super().__init__()
        self.size = size
        self.pos = pos
        self.rect = self.rend.get_rect()
        self.rect.size = self.size

    def update(self):
        py.draw.rect(v.screen, v.black, self.rect)



