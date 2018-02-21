
# =========================================================================== #
""" Physics Engine Tests and planning program """
# =========================================================================== #


import Physics_Engine_Test as physics
import MenuItems as menu
import GameItems as game
import Variables as v
import Objects as o
import pygame as py
import random
import sys


'''Defining Sprites and Objects'''
# Particles: (pos, size, colour=v.black, thickness=1, velocity=0)
particles = []
for i in range(v.noOfParticles):
    random_size = random.randint(10, 20)
    random_pos = (random.randint(random_size, v.width - random_size), random.randint(random_size, v.height - random_size))
    particles.append(physics.particle(random_pos, random_size))


# Buttons: (text, textColour, textSize, pos, buttonColour, ID, buttonSize=(0, 0), textCentred=False, centred=False)


# Text Labels: (text, textColour, textSize, pos, labelColour, centred=False)


class loops:
    def __init__(self):
        py.init()
        v.screen = py.display.set_mode(v.size)
        py.display.set_caption("Physics Engine Tests")
        v.screen.fill(v.white)

    def quit_check(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()

    def main_menu(self):
        while True:
            self.quit_check()

            for i in particles:
                i.display()

            py.display.flip()

    def game_loop(self):
        while True:
            self.quit_check()


if __name__ == "__main__":
    L = loops()
    L.main_menu()




