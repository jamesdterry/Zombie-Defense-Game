#
# Screen
#

import pygame
import sys
import os

FREQ = 22060   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 1   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished


class Screen:

    screen = None
    size = None

    def __init__(self):
        pass

    def MakeScreen(self, width, height):
        pygame.mixer.pre_init(FREQ, BITSIZE, CHANNELS, BUFFER)
        pygame.init()
        pygame.mouse.set_visible(False)

        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
                # Make sure that SDL_VIDEODRIVER is set
                if not os.getenv('SDL_VIDEODRIVER'):
                        os.putenv('SDL_VIDEODRIVER', driver)
                        try:
                                pygame.display.init()
                        except pygame.error:
                                print 'Driver: {0} failed.'.format(driver)
                                continue
                        found = True
                        break

        if not found:
            raise Exception('No suitable video driver found!')

        infoObject = pygame.display.Info()

        self.size = (width, height)
        self.screen = pygame.display.set_mode((width, height))
