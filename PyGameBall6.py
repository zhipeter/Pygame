'''
This is a Pygame Ball game
'''
import sys
import pygame

class Settings():
    '''储存设置的类'''
pygame.init()
Size = width, height = 600, 400
Speed = [1, 1]
BLACK = 0, 55, 55
Screen = pygame.display.set_mode(Size, pygame.RESIZABLE)
pygame.display.set_caption("BALL GAME")
Ball = pygame.image.load("PYG02-ball.gif")
Ballrect = Ball.get_rect()
fps = 300
fclock = pygame.time.Clock()
still = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Speed[0] = Speed[0] if Speed[0] == 0 else (
                    abs(Speed[0]) - 1) * int(Speed[0] / abs(Speed[0]))
            elif event.key == pygame.K_RIGHT:
                Speed[0] = Speed[0] + 1 if Speed[0] > 0 else Speed[0] - 1
            elif event.key == pygame.K_UP:
                Speed[1] = Speed[1] + 1 if Speed[1] > 0 else Speed[0] - 1
            elif event.key == pygame.K_DOWN:
                Speed[1] = Speed[1] if Speed[1] == 0 else (
                    abs(Speed[1]) - 1) * int(Speed[1] / abs(Speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            Size = width, height = event.size[0], event.size[1]
            Screen = pygame.display.set_mode(Size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                Ballrect = Ballrect.move(event.pos[0] - Ballrect.left,
                                         event.pos[1] - Ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                Ballrect = Ballrect.move(event.pos[0] - Ballrect.left,
                                         event.pos[1] - Ballrect.top)
    if pygame.display.get_active():
        Ballrect = Ballrect.move(Speed)
    if Ballrect.left < 0 or Ballrect.right > width:
        Speed[0] = -Speed[0]
    if Ballrect.top < 0 or Ballrect.bottom > height:
        Speed[1] = -Speed[1]

    Screen.fill(BLACK)
    Screen.blit(Ball, Ballrect)
    pygame.display.update()
    fclock.tick(fps)
