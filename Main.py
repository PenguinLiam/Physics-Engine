
# =========================================================================== #
''' Physics Engine Tests and planning program '''
# =========================================================================== #


import Physics_Engine_Test as physics
import MenuItems as menu
import GameItems as game
import Variables as v
import Objects as o
import pygame as py
import random
import sys



class loops:
    def __init__(self):
        py.init()
        v.screen = py.display.set_mode(v.size)
        py.display.set_caption("Physics Engine Tests")
        v.screen.fill(v.screenColour)


    # Sub-routine for checking whether the program window is closed
    def quit_check(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()


    # Starting page loop - contains run button, settings and other functions
    def main_menu(self):
        while True:
            self.quit_check()

            for i in o.particles:
                i.display()

            py.display.flip()

    def game_loop(self):
        while True:
            self.quit_check()


if __name__ == "__main__":
    L = loops()
    L.main_menu()