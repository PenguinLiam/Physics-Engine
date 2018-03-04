
# =========================================================================== #
""" Physics Engine Tests Main """
# =========================================================================== #


import Physics_Engine_Test as physics
import MenuItems as menu
import GameItems as game
import Variables as v
import Objects as o
import pygame as py
import sys


class Loops:
    def __init__(self):
        py.init()
        v.screen = py.display.set_mode(v.size, py.RESIZABLE)
        py.display.set_caption("Physics Engine Tests")
        v.screen.fill(v.white)

    @staticmethod
    def quit_check():
        for event in v.events:
            if event.type == py.QUIT:
                sys.exit()
            if event.type == py.VIDEORESIZE:
                py.display.set_mode(event.size, py.RESIZABLE)
                v.size = event.size

    def main_menu(self):
        while True:
            v.events = py.event.get()
            self.quit_check()
            v.screen.fill(v.white)

            for event in v.events:
                if event.type == py.KEYDOWN:
                    self.game_loop()

            py.display.flip()

    def game_loop(self):
        clock = py.time.Clock()
        while True:
            clock.tick(60)
            v.events = py.event.get()
            self.quit_check()

            v.screen.fill(v.white)
            for i in o.particles:
                i.draw()
                i.move()
                i.update()

            # Movement for selected particles
            keys = py.key.get_pressed()
            if keys[py.K_LEFT]:
                for i in o.particles:
                    if i.selected:
                        i.velocity[0] -= 0.5
            elif keys[py.K_RIGHT]:
                for i in o.particles:
                    if i.selected:
                        i.velocity[0] += 0.5
            elif keys[py.K_UP]:
                for i in o.particles:
                    if i.selected:
                        i.velocity[1] -= 0.5
            elif keys[py.K_DOWN]:
                for i in o.particles:
                    if i.selected:
                        i.velocity[1] += 0.5

            py.display.flip()


if __name__ == "__main__":
    L = Loops()
    L.main_menu()




