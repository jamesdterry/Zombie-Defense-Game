#
# Base Scene for Zombie Game
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from scene import Scene

TEXTCOLOR = (255, 255, 255)

class BaseZombieScene(Scene):

    def drawText(self, text, font, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.s.screen.blit(textobj, textrect)


