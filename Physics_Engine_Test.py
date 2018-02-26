
# =========================================================================== #
""" Physics Engine Tests """
# =========================================================================== #


import MenuItems as menu
import GameItems as game
import Variables as v
import pygame as py
import math
import sys


'''
SUVAT EQUATIONS

s = ut + 1/2 at^2

s = vt - 1/2 at^2

v = u + at

s = 1/2 (u + v)t

v^2 = u^2 + 2 as

NOTES
---> is positive velocity and displacement  }
<--- is negative velocity and displacement  } Verticle velocities

Up is also positive velocity and displacement    }
down is also negative velocity and displacement  } Horizontal velocities

drag = 0.75
velocity *= drag
'''

# Particle
class particle(py.sprite.Sprite):
    def __init__(self, pos, size, colour=v.black, thickness=1, selected=False):
        super().__init__()
        self.pos = list(pos)
        self.size = size
        self.colour = colour
        self.__colour = colour
        self.hoveredColour = (0, 0, 255)
        self.selectedColour = (255, 0, 0)
        self.thickness = thickness
        self.velocity = [0, 0]
        self.rect = py.Rect(0, 0, size * 2, size * 2)
        self.hovered = False
        self.selected = selected
        
    def draw(self):
        py.draw.circle(v.screen, self.colour, self.rect.center, self.size, self.thickness)

    def update(self):
        self.pos[0] += int(self.velocity[0])
        self.pos[1] += int(self.velocity[1])

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


        self.rect.center = self.pos



class projectile():
    '''Manages accurate movement of projectiles

    Requires unit vectors for vertical and horizontal (i & j respectively).
    Uses equation s = ut + 1/2 at^2 
    '''
    def __init__(self, item, **kwargs):
        # Initialising Main Variables
        self.item = item

        # Initialising Kwargs
        if kwargs is not None:
            try:
                for key, value in kwargs.iteritems():
                    if key.lower() == "s": # Displacement
                        self.S = value
                    elif key.lower() == "u": # Initial Velocity
                        self.U = value
                    elif key.lower() == "v": # Final Velocity
                        self.V = value
                    elif key.lower() == "a": # Acceleration
                        self.A = value
                    elif key.lower() == "t": # Time
                        self.T = value
            except:
                print("keyword arguments must be SUVAT. Note, not all variables are required")

    def update(self):
        pass


