
# Menu Items File #

import Variables as v
import pygame as py



# Button
class Button(py.sprite.Sprite):
    def __init__(self, text, textColour, textSize, pos, buttonColour, ID, buttonSize=(0, 0), textCentred=False, centred=False):
        super().__init__()

        # Initialising Arguments
        self.text = text
        self.textColour = textColour
        self.textSize = textSize
        self.pos = pos
        self.buttonColour = buttonColour
        self.ID = ID
        
        # Initialising the Status of the Buttons
        self.hovered = False
        self.pressed = False

        # Size and Centering Conditions
        if not buttonSize == (0, 0):
            self.rect.size = buttonSize
        if centred:
            self.rect.centre = self.pos
        else:
            self.rect.topleft = self.pos

    def update(self):
        # Hover Checking and Updating
        if self.rect.collidepoint(py.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

        for event in v.events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.hovered:
                    self.pressed = True


# Label
class Label(py.sprite.Sprite):
    def __init__(self, text, textColour, textSize, pos, labelColour, centred=False):
        super().__init__()
        
        # Initialising Arguments
        self.text = text
        self.textColour = textColour
        self.textSize = textSize
        self.pos = pos
        self.labelColour = labelColour

        # Initialising Text Conditions
        self.font = py.font.SysFont(font, self.textSize)
        self.rend = self.font.render(self.text, 1, self.textColour)

        # Size and Centering Conditions
        self.centred = centred

    def update(self):
        if self.centred:
            v.screen.blit(self.rend, self.pos)
        else:
            rect = self.rend.get_rect()
            rect.center = self.pos
            v.screen.blit(self.rend, rect)




