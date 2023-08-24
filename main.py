import pygame, sys
from grid import Grid
from pieces import *

pygame.init()

# Create the screen
screen = pygame.display.set_mode((300, 600))

# Title and Icon
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


# Game Loop
running = True

game_grid = Grid(10, 20, 30)
piece = Spiece()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    # RGB = Red, Green, Blue
    screen.fill((10, 10, 10))
    game_grid.draw_grid(screen)
    piece.draw_shape(screen)
    pygame.display.update()
