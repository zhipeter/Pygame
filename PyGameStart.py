'''
This is a Python Pygame Hello World Program
'''
import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PyGame Start")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
