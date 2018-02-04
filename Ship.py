'''
This is a Class of Ship
'''

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    ''' a Class of Ship'''

    def __init__(self, set, screen):
        '''init ship'''
        super(Ship, self).__init__()
        self.screen = screen
        self.set = set

        # load ship
        self.image = pygame.image.load('Ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # puy ship on bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # at the 'center' save float
        self.center = float(self.rect.centerx)

        # move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update ship location'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.set.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.set.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        '''draw ship on the point'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''center ship'''
        self.center = self.screen_rect.centerx
