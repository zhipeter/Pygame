'''
This is a class of scoreboard
'''
import pygame.font
from pygame.sprite import Group
from Ship import Ship


class Scoreboard():
    '''show score'''

    def __init__(self, set, screen, stats):
        '''init score'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.set = set
        self.stats = stats

        # font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # init score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''change score into image'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.set.bg_color)

        # put score image on
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''change high score into image'''
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.set.bg_color)

        # put high score image on center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        '''change level into image'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                                            self.set.bg_color)

        # put level image on
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''show ships'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.set, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        '''show score'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
