#
# Simple Sprite
#

import pygame
import os

from screen import Screen

class Sprite:
    bitmap = None
    x = 0
    y = 0

    def __init__(self, filename):
        self.bitmap = pygame.image.load(filename)

    def blit(self, s):
        s.screen.blit(self.bitmap, (self.x, self.y))

    def blit_at(self, s, x, y):
        self.x = x
        self.y = y
        s.screen.blit(self.bitmap, (self.x, self.y))

    def width(self):
        return self.bitmap.get_width()

    def height(self):
        return self.bitmap.get_height()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.bitmap.get_width(), self.bitmap.get_height())

    def collide(self, other_sprite):
        my_rect = self.rect()
        other_rect = other_sprite.rect()
        return my_rect.colliderect(other_rect)

