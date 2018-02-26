
# =========================================================================== #
""" Objects """
# =========================================================================== #

import Physics_Engine_Test as physics
import MenuItems as menu
import GameItems as game
import Variables as v
import pygame as py
import random
import sys


'''Defining Sprites and Objects'''
# Particles: (pos, size, colour=v.black, thickness=1, velocity=[0, 0], selected=False)
particles = []
for i in range(v.noOfParticles):
    random_size = random.randint(10, 20)
    random_pos = (random.randint(random_size, v.width - random_size), random.randint(random_size, v.height - random_size))
    particles.append(physics.particle(random_pos, random_size))


# Buttons: (text, textColour, textSize, pos, buttonColour, ID, buttonSize=(0, 0), textCentred=False, centred=False)


# Text Labels: (text, textColour, textSize, pos, labelColour, centred=False)