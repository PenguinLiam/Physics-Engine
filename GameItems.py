
# =========================================================================== #
""" Game Items """
# =========================================================================== #

import pygame as py
import Variables as v
import math
import random


# Particle class - Needs fixing in relation to velocity and movement for all particles
class Particle(py.sprite.Sprite):
    def __init__(self, pos, size, colour=v.black, thickness=1, selected=False):
        super().__init__()  # Sprite class doesnt require any arguments
        self.pos = list(pos)
        self.size = size
        self.colour = colour
        self.__colour = colour  # For returning the colour to the original colour when de-selected
        self.hoveredColour = (0, 0, 255)
        self.selectedColour = (255, 0, 0)
        self.thickness = thickness
        self.velocity = [1, 1]
        self.__speed = 0
        self.__angle = (random.randint(0, 360) * (math.pi / 180))
        self.rect = py.Rect(0, 0, size * 2, size * 2)
        self.hovered = False
        self.selected = selected

    def draw(self):
        py.draw.circle(v.screen, self.colour, self.rect.center, self.size, self.thickness)

    def update(self):
        self.velocity[0] *= 0.99
        self.velocity[1] *= 0.99

        # Hover Checking and Updating
        if self.rect.collidepoint(py.mouse.get_pos()):
            self.hovered = True
            self.colour = self.hoveredColour
        else:
            self.hovered = False
            self.colour = self.__colour

        for event in v.events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.hovered:
                    self.selected = not self.selected

        if self.selected:
            self.colour = self.selectedColour

            self.pos[0] += int(self.velocity[0])  # X direction
            self.pos[1] += int(self.velocity[1])  # Y direction

            # Try dot product to find the angle so that bounces can work between (un)interacted particles - redo...
            self.__angle = (math.atan(self.velocity[1] / self.velocity[0]) * (math.pi / 180))
            print(self.__angle)
        else:
            # Speed can only be positive because the hypot us a length, not a direction - maybe rethink...?
            self.__speed = math.hypot(self.velocity[0], self.velocity[1])

        self.rect.center = self.pos

    def move(self):
        self.pos[0] += math.sin(self.__angle) * self.__speed
        self.pos[1] += math.cos(self.__angle) * self.__speed

