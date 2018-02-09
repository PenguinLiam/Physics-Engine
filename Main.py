
# =========================================================================== #
""" Physics Engine Tests and planning program """
# =========================================================================== #


import Physics_Engine_Test as physics
import MenuItems as menu
import GameItems as game
import Variables as v
import pygame as py
import sys


def MainMenu():
    py.init()
    v.screen = py.display.set_mode(v.size)
    py.display.set_caption("Physics Testing")
    v.screen.fill(v.white)
    while True:
        for event in py.event.get():
            # Exit Checking
            if event.type == py.Quit():
                sys.exit()

            # Movement Controls - (currently arros keys)
            if event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    sprite=pygame.image.load('left.png')
                elif (event.key == K_RIGHT):
                    sprite=pygame.image.load('right.png')
                elif (event.key == K_UP):
                    sprite=pygame.image.load('up.png')
                elif (event.key == K_DOWN):
                    sprite=pygame.image.load('down.png')

    py.display.flip()


if __name__ == "__main__":
    MainMenu()





