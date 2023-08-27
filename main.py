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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.current_piece.move("left")
                if not game.grid.is_valid(game.current_piece):
                    game.current_piece.move("right")

            if event.key == pygame.K_RIGHT:
                game.current_piece.move("right")
                if not game.grid.is_valid(game.current_piece):
                    game.current_piece.move("left")

            if event.key == pygame.K_DOWN:
                game.current_piece.move("down")
                if not game.grid.is_valid(game.current_piece):
                    game.current_piece.move("up")

            if event.key == pygame.K_UP:
                game.current_piece.rotate()
                if not game.grid.is_valid(game.current_piece):
                    game.current_piece.rotate_back()

    # RGB = Red, Green, Blue
    screen.fill((10, 10, 10))
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
