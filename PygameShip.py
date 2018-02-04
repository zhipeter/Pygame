'''
This is a Pygame Ship game
'''

import pygame
from pygame.sprite import Group
from Settings import Settings
from Ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    '''run game'''
    pygame.init()
    set = Settings()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Ship GAME")

    # create a ship
    ship = Ship(set, screen)
    # create a group saving bullets
    bullets = Group()
    # create an alien
    aliens = Group()
    # create aliens
    gf.create_fleet(set, screen, ship, aliens)
    # create game stats and score
    stats = GameStats(set)
    sb = Scoreboard(set, screen, stats)
    # create button
    play_button = Button(set, screen, "Play")

    # start game circle
    while True:
        gf.check_events(set, screen, stats, sb, play_button, ship, aliens,
                        bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(set, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(set, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(set, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()
