import pygame
from game import Game

pygame.init()

# Create the screen
screen = pygame.display.set_mode((300, 600))

# Title and Icon
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game.game_over:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_piece("left")
            if event.key == pygame.K_RIGHT:
                game.move_piece("right")
            if event.key == pygame.K_DOWN:
                game.move_piece("down")
            if event.key == pygame.K_UP:
                game.rotate_piece()
        if event.type == GAME_UPDATE:
            game.move_piece("down")

    # RGB = Red, Green, Blue
    screen.fill((10, 10, 10))
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
