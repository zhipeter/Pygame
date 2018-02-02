'''
This is a Class of alien
'''
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''class of an alien'''

    def __init__(self, set, screen):
        '''init alien and position'''
        super(Alien, self).__init__()
        self.screen = screen
        self.set = set

        # load alien image
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect()

        # firstly put alien on the (0,0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save alien position
        self.x = float(self.rect.x)

    def blitme(self):
        '''draw alien'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''move aliens'''
        self.x += (self.set.alien_speed_factor * self.set.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''check edges'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True