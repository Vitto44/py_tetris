import pygame
from game import Game

pygame.init()

# Create the screen
screen = pygame.display.set_mode((300, 600))

# Title and Icon
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

game = Game()

# Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB = Red, Green, Blue
    screen.fill((10, 10, 10))
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
