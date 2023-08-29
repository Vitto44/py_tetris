import pygame
from game import Game

pygame.init()

# Add Font
title_font = pygame.font.SysFont("minecraft.ttf", 80)
normal_text_fond = pygame.font.SysFont("minecraft.ttf", 30)
game_over_font = pygame.font.SysFont("minecraft.ttf", 100)

title_surface = title_font.render("Tetris", True, (0, 255, 0))
score_surface = normal_text_fond.render("Score: ", True, (0, 255, 0))
game_over_surface = game_over_font.render("GAME OVER", True, (0, 255, 0))
next_piece_surface = normal_text_fond.render("Next Piece: ", True, (0, 255, 0))
next_piece_rect = next_piece_surface.get_rect(center=(900 // 2, 400))

# Create the screen
screen = pygame.display.set_mode((600, 620))

# Title and Icon
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 500)

# Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not game.grid.game_over:
                game.move_piece("left")
            if event.key == pygame.K_RIGHT and not game.grid.game_over:
                game.move_piece("right")
            if event.key == pygame.K_DOWN and not game.grid.game_over:
                game.move_piece("down")
            if event.key == pygame.K_UP and not game.grid.game_over:
                game.rotate_piece()
        if game.grid.game_over:
            print("GAME OVER")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.reset()
        if event.type == GAME_UPDATE and not game.grid.game_over:
            game.move_piece("down")

    # RGB = Red, Green, Blue
    screen.fill((10, 10, 10))
    # TITLE
    screen.blit(title_surface, ((900 - title_surface.get_width()) // 2, 20))
    # SCORE
    screen.blit(score_surface, ((900 - score_surface.get_width()) // 2, 150))
    # SCORE NUMBER
    normal_text_surface = normal_text_fond.render(str(game.score), True, (0, 255, 0))
    screen.blit(
        normal_text_surface, ((900 - normal_text_surface.get_width()) // 2, 180)
    )
    # NEXT PIECE
    screen.blit(next_piece_surface, ((900 - next_piece_surface.get_width()) // 2, 350))
    # NEXT PIECE ILLUSTRATION
    pygame.draw.rect(screen, (0, 255, 0), next_piece_rect, 1)
    # GAME OVER
    if game.grid.game_over:
        screen.blit(
            game_over_surface, ((600 - game_over_surface.get_width()) // 2, 200)
        )

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
