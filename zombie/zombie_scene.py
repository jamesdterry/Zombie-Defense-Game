#
# Main Zombie Game Scene
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from BaseZombieScene import BaseZombieScene

import over_scene

MAXGOTTENPASS = 10
ZOMBIESIZE = 70
ADDNEWZOMBIERATE = 30
ADDNEWKINDZOMBIE = ADDNEWZOMBIERATE

NORMALZOMBIESPEED = 2
NEWKINDZOMBIESPEED = NORMALZOMBIESPEED / 2

PLAYERMOVERATE = 15
BULLETSPEED = 10
ADDNEWBULLETRATE = 15

class zombie_scene(BaseZombieScene):
    font = None
    game_over = False

    zombies = []
    newKindZombies = []
    bullets = []

    zombiesGottenPast = 0
    score = 0

    # playerRect.topleft = (50, WINDOWHEIGHT /2)
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    shoot = False

    zombieAddCounter = 0
    newKindZombieAddCounter = 0
    bulletAddCounter = 0

    zombieImage = None
    newKindZombieImage = None
    playerImage = None
    playerRect = None
    bulletImage = None
    bulletRect = None

    death_by_zombie = False

    def playerHasHitZombie(self, playerRect, zombies):
        for z in zombies:
            if playerRect.colliderect(z.rect()):
                return True
        return False

    def bulletHasHitZombie(self, z, bullets, zombies):
        for b in bullets:
            if b.collide(z):
                bullets.remove(b)
                return True
        return False

    def bulletHasHitCrawler(self, c, bullets, newKindZombies):
        for b in bullets:
            if b.collide(c):
                bullets.remove(b)
                return True
        return False


    def load(self):
        self.font = pygame.font.SysFont(None, 48)
        self.zombies = []
        self.newKindZombies = []
        self.bullets = []
        self.playerImage = Sprite.fromfile('SnowPea.gif')
        self.playerRect = self.playerImage.rect()
        self.playerRect.topleft = (50, self.s.size[1] / 2)
        self.zombieImage = Sprite.fromfile('tree.png')
        self.newKindZombieImage = Sprite.fromfile('ConeheadZombieAttack.gif')
        self.bulletImage = Sprite.fromfile('SnowPeashooterBullet.gif')
        self.bulletRect = self.bulletImage.rect()
        self.bulletAddCounter = 40
        self.death_by_zombie = False

    def cleanup(self):
        pass

    def do_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.moveDown = True
                self.moveUp = False
            elif event.key == pygame.K_UP:
                self.moveDown = False
                self.moveUp = True
            elif event.key == pygame.K_SPACE:
                self.shoot = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.moveDown = False
            elif event.key == pygame.K_UP:
                self.moveUp = False
            elif event.key == pygame.K_SPACE:
                self.shoot = False

    def update(self):
        # Add new zombies at the top of the screen, if needed.
        self.zombieAddCounter += 1
        if self.zombieAddCounter == ADDNEWKINDZOMBIE:
            self.zombieAddCounter = 0
            zombieSize = ZOMBIESIZE
            newZombie = Sprite.clone(self.zombieImage, (zombieSize, zombieSize))
            newZombie.x = self.s.size[0]
            newZombie.y = random.randint(10, self.s.size[1] - zombieSize - 10)
            self.zombies.append(newZombie)

        # Add new newKindZombies at the top of the screen, if needed.
        self.newKindZombieAddCounter += 1
        if self.newKindZombieAddCounter == ADDNEWZOMBIERATE:
            self.newKindZombieAddCounter = 0
            newKindZombiesize = ZOMBIESIZE
            newCrawler = Sprite.clone(self.newKindZombieImage, (newKindZombiesize, newKindZombiesize))
            newCrawler.x = self.s.size[0]
            newCrawler.y = random.randint(10, self.s.size[1] - newKindZombiesize - 10)
            self.newKindZombies.append(newCrawler)

        # add new bullet
        self.bulletAddCounter += 1
        if self.bulletAddCounter >= ADDNEWBULLETRATE and self.shoot == True:
            self.bulletAddCounter = 0
            newBullet = Sprite.clone(self.bulletImage, (self.bulletRect.width, self.bulletRect.height))
            newBullet.x = self.playerRect.centerx + 10
            newBullet.y = self.playerRect.centery - 25
            self.bullets.append(newBullet)

        # Move the player around.
        if self.moveUp and self.playerRect.top > 30:
            self.playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if self.moveDown and self.playerRect.bottom < self.s.size[1] - 10:
            self.playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the zombies down.
        for z in self.zombies:
            z.x = z.x - NORMALZOMBIESPEED

        # Move the newKindZombies down.
        for c in self.newKindZombies:
            c.x = c.x - NEWKINDZOMBIESPEED

        # move the bullet
        for b in self.bullets:
            b.x = b.x + BULLETSPEED

        # Delete zombies that have fallen past the bottom.
        for z in self.zombies[:]:
            if z.rect().left < 0:
                self.zombies.remove(z)
                self.zombiesGottenPast += 1

        # Delete newKindZombies that have fallen past the bottom.
        for c in self.newKindZombies[:]:
            if c.rect().left < 0:
                self.newKindZombies.remove(c)
                self.zombiesGottenPast += 1

        for b in self.bullets[:]:
            if b.rect().right > self.s.size[0]:
                self.bullets.remove(b)

        # check if the bullet has hit the zombie
        for z in self.zombies:
            if self.bulletHasHitZombie(z, self.bullets, self.zombies):
                self.score += 1
                self.zombies.remove(z)

        for c in self.newKindZombies:
            if self.bulletHasHitCrawler(c, self.bullets, self.newKindZombies):
                self.score += 1
                self.newKindZombies.remove(c)

        # Check if any of the zombies has hit the player.
        if self.playerHasHitZombie(self.playerRect, self.zombies):
            self.death_by_zombie = True
            self.game_over = True

        if self.playerHasHitZombie(self.playerRect, self.newKindZombies):
            self.death_by_zombie = True
            self.game_over = True

        # check if score is over MAXGOTTENPASS which means game over
        if self.zombiesGottenPast >= MAXGOTTENPASS:
            self.game_over = True


    def draw(self):
        self.s.screen.blit(self.game.rescaledBackground, (0, 0))

        # Draw the player's rectangle, rails
        self.playerImage.blit_at_rect(self.s, self.playerRect)

        # Draw each baddie
        for z in self.zombies:
            z.blit(self.s)

        for c in self.newKindZombies:
            c.blit(self.s)

        # draw each bullet
        for b in self.bullets:
            b.blit(self.s)

        # Draw the score and how many zombies got past
        self.drawText('zombies gotten past: %s' % (self.zombiesGottenPast), self.font, 10, 20)
        self.drawText('score: %s' % (self.score), self.font, 10, 50)

        if self.game_over:
            os = over_scene.over_scene(self.game)
            os.score = self.score
            os.death_by_zombie = self.death_by_zombie
            self.game.gotoScene(os)
