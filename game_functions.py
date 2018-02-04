'''
Game functions
'''
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, set, screen, ship, bullets):
    '''response key down'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(set, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def fire_bullet(set, screen, ship, bullets):
    ''' fire a bullet before the limit'''
    if len(bullets) < set.bullets_allowed:
        new_bullet = Bullet(set, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    '''response key up'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(set, screen, stats, sb, play_button, ship, aliens, bullets):
    '''response events from click or buttons'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, set, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(set, screen, stats, sb, play_button, ship, aliens,
                              bullets, mouse_x, mouse_y)


def check_play_button(set, screen, stats, sb, play_button, ship, aliens, bullets,
                      mouse_x, mouse_y):
    '''start new game'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game settings
        set.initialize_dynamic_settings()
        # set mouse visible
        pygame.mouse.set_visible(False)
        # reset game stats
        stats.reset_stats()
        stats.game_active = True

        # reset score image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # clear out aliens and bullets
        aliens.empty()
        bullets.empty()

        # create new aliens
        create_fleet(set, screen, ship, aliens)
        ship.center_ship()


def update_screen(set, screen, stats, sb, ship, aliens, bullets, play_button):
    '''update screen'''
    screen.fill(set.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # show score
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(set, screen, stats, sb, ship, aliens, bullets):
    '''update bullet position and delete bullets'''
    # update bullet position
    bullets.update()

    # delete bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(set, screen, stats, sb, ship, aliens,
                                  bullets)


def check_bullet_alien_collisions(set, screen, stats, sb, ship, aliens,
                                  bullets):
    '''response collision of bullet and aliens'''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += set.alien_points
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        set.increase_speed()

        # increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(set, screen, ship, aliens)


def get_number_aliens_x(set, alien_width):
    '''get numbers of each line'''
    available_space_x = set.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(set, ship_height, alien_height):
    '''get numbers of rows'''
    available_space_y = (set.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(set, screen, aliens, alien_number, row_number):
    '''create an alien'''
    alien = Alien(set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(set, screen, ship, aliens):
    '''create aliens fleet'''
    alien = Alien(set, screen)
    number_aliens_x = get_number_aliens_x(set, alien.rect.width)
    number_rows = get_number_rows(set, ship.rect.height, alien.rect.height)

    # create first line alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(set, screen, aliens, alien_number, row_number)


def check_fleet_edges(set, aliens):
    '''take measures when aliens arrive edges'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(set, aliens)
            break


def change_fleet_direction(set, aliens):
    '''move down aliens and change fleet direction'''
    for alien in aliens.sprites():
        alien.rect.y += set.fleet_drop_speed
    set.fleet_direction *= -1


def ship_hit(set, screen, stats, sb, ship, aliens, bullets):
    '''response ship hitted'''
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        # clear out alien and bullet
        aliens.empty()
        bullets.empty()
        # create new aliens
        create_fleet(set, screen, ship, aliens)
        ship.center_ship()
        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(set, screen, stats, sb, ship, aliens, bullets):
    '''check if aliens arrive bottom'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(set, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(set, screen, stats, sb, ship, aliens, bullets):
    '''update aliens'''
    check_fleet_edges(set, aliens)
    aliens.update()

    # collisions of alien and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(set, screen, stats, sb, ship, aliens, bullets)

    # check if aliens arrive bottom
    check_aliens_bottom(set, screen, stats, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    '''check if exits high score'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
