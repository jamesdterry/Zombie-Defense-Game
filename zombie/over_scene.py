#
# Game Over Scene
#

import pygame
import random
import pickle

from screen import Screen
from sprite import Sprite
from BaseZombieScene import BaseZombieScene

import intro_scene

ALLOW_EXIT = pygame.USEREVENT + 2

class over_scene(BaseZombieScene):
    font = None
    allow_exit = False
    playerImage = None
    score = 0
    death_by_zombie = False

    def load(self):
        self.s.screen.fill((0,0,0))
        self.font = pygame.font.SysFont(None, 48)
        self.playerImage = pygame.image.load('art/SnowPea.gif')

        pygame.time.set_timer(ALLOW_EXIT, 1000 * 5)

        gameOverSound = pygame.mixer.Sound('art/gameover.wav')
        gameOverSound.play()

    def do_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                if self.allow_exit:
                    self.game.gotoScene(intro_scene.intro_scene(self.game))
        elif event.type == ALLOW_EXIT:
            self.allow_exit = True
            pygame.time.set_timer(ALLOW_EXIT, 0)

    def cleanup(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.s.screen.blit(self.game.rescaledBackground, (0, 0))
        self.s.screen.blit(self.playerImage, (self.s.size[0] / 2, self.s.size[1] - 70))
        self.drawText('score: %s' % (self.score), self.font, 10, 30)
        if self.death_by_zombie:
            self.drawText('GAME OVER', self.font, (self.s.size[0] / 3), (self.s.size[1] / 3))
            self.drawText('YOU HAVE BEEN KISSED BY THE ZOMBIE', self.font, (self.s.size[0] / 4) - 80, (self.s.size[1] / 3) +100)
            self.drawText('Press enter to play again or escape to exit', self.font, (self.s.size[0] / 4) - 80, (self.s.size[1] / 3) + 150)
        else:
            self.drawText('GAME OVER', self.font, (self.s.size[0] / 3), (self.s.size[1] / 3))
            self.drawText('YOUR COUNTRY HAS BEEN DESTROYED', self.font, (self.s.size[0] / 4)- 80, (self.s.size[1] / 3) + 100)
            self.drawText('Press enter to play again or escape to exit', self.font, (self.s.size[0] / 4) - 80, (self.s.size[1] / 3) + 150)

