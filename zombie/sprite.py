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

    @classmethod
    def fromfile(cls, filename):
        sprite = cls()
        sprite.bitmap = pygame.image.load(filename)
        return sprite

    @classmethod
    def clone(cls, base_sprite, size):
        sprite = cls()
        sprite.bitmap = pygame.transform.scale(base_sprite.bitmap, size)
        return sprite

    def blit(self, s):
        s.screen.blit(self.bitmap, (self.x, self.y))

    def blit_at(self, s, x, y):
        self.x = x
        self.y = y
        s.screen.blit(self.bitmap, (self.x, self.y))

    def blit_at_rect(self, s, r):
        self.x = r.topleft[0]
        self.y = r.topleft[1]
        s.screen.blit(self.bitmap, r)

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

    def colliderect(self, other_rect):
        my_rect = self.rect()
        return my_rect.colliderect(other_rect)
