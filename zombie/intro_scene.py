#
# Intro Scene
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from scene import Scene

import zombie_scene

TEXTCOLOR = (255, 255, 255)

class intro_scene(Scene):
    font = None
    playerImage = None

    def load(self):
        self.font = pygame.font.SysFont(None, 48)
        self.playerImage = pygame.image.load('SnowPea.gif')

        print self.s.size[0], self.s.size[1]

    def cleanup(self):
        pass

    def do_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.game.gotoScene(zombie_scene.zombie_scene(self.game))

    def update(self):
        pass

    def drawText(self, text, font, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.s.screen.blit(textobj, textrect)

    def draw(self):
        self.s.screen.blit(self.game.rescaledBackground, (0, 0))

        self.s.screen.blit(self.playerImage, (self.s.size[0] / 2, self.s.size[1] - 70))
        self.drawText('Zombie Defense By handsomestone', self.font, (self.s.size[0] / 4), (self.s.size[1] / 4))
        self.drawText('Press Enter to start', self.font, (self.s.size[0] / 3) - 10, (self.s.size[1] / 3) + 50)

