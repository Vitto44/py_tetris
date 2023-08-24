import pygame, sys
from grid import Grid

pygame.init()

# Create the screen
screen = pygame.display.set_mode((300, 600))

# Title and Icon
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


# Game Loop
running = True

game_grid = Grid(10, 20)

game_grid.grid[0][1] = 1

game_grid.print_grid()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    # RGB = Red, Green, Blue
    screen.fill((10, 10, 10))
    game_grid.draw_grid(screen)
    pygame.display.update()
