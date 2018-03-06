
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


# Not a functioning class...

class Projectile:
    """Manages accurate movement of projectiles

    Requires unit vectors for vertical and horizontal (i & j respectively).
    Uses equation s = ut + 1/2 at^2 
    """
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


