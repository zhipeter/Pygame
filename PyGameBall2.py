'''
This is a Pygame Ball game
'''
import sys
import pygame

pygame.init()
Size = width, height = 600, 400
Speed = [1, 1]
BLACK = 0, 0, 0
Screen = pygame.display.set_mode(Size)
pygame.display.set_caption("BALL GAME")
Ball = pygame.image.load("PYG02-ball.gif")
Ballrect = Ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    Ballrect = Ballrect.move(Speed[0], Speed[1])
    if Ballrect.left < 0 or Ballrect.right > width:
        Speed[0] = -Speed[0]
    if Ballrect.top < 0 or Ballrect.bottom > height:
        Speed[1] = -Speed[1]

    Screen.fill(BLACK)
    Screen.blit(Ball, Ballrect)
    pygame.display.update()
    fclock.tick(fps)
