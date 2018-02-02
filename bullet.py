'''
This is a Class of bullets
'''
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''manage bullet from ship'''

    def __init__(self, set, screen, ship):
        '''create bullet at ship position'''
        super(Bullet, self).__init__()
        self.screen = screen

        # creat bullet rect
        self.rect = pygame.Rect(0, 0, set.bullet_width, set.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # save bullet position by float
        self.y = float(self.rect.y)

        self.color = set.bullet_color
        self.speed_factor = set.bullet_speed_factor

    def update(self):
        '''move bullet up'''
        # update bullet position float
        self.y -= self.speed_factor
        # update bullet rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw bullet'''
        pygame.draw.rect(self.screen, self.color, self.rect)
