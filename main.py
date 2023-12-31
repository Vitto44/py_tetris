import pygame
from game import Game

pygame.init()


# Add Font
title_font = pygame.font.Font("fonts/Minecraft.ttf", 70)
normal_text_fond = pygame.font.Font("fonts/Minecraft.ttf", 30)
game_over_font = pygame.font.Font("fonts/Minecraft.ttf", 80)

title_surface = title_font.render("Tetris", True, (0, 255, 0))
score_surface = normal_text_fond.render("Score: ", True, (0, 255, 0))
top_score_surface = normal_text_fond.render("Top 3 Scores: ", True, (0, 255, 0))
game_over_surface = game_over_font.render("GAME OVER", True, (0, 255, 0))
next_piece_surface = normal_text_fond.render("Next Piece: ", True, (0, 255, 0))
restart_or_quit_surface = normal_text_fond.render(
    "Press SPACE to restart or Q to quit", True, (0, 255, 0)
)
game_over_rect = pygame.Rect(30, 140, 540, 230)

# Create the screen
screen_width = 600
screen_height = 620
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 600)

# check scores file and get top 3 scores
try:
    f = open("scores.txt", "r+")
except FileNotFoundError:
    f = open("scores.txt", "w+")
# write top 3 scores to file
scores = []
for line in f:
    scores.append(int(line))

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
                game.score += 1
                game.move_piece("down")
            if event.key == pygame.K_UP and not game.grid.game_over:
                game.rotate_piece()
        if game.grid.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scores.append(game.score)
                    game.reset()
                    scores.sort(reverse=True)
                    scores = scores[:3]
                if event.key == pygame.K_q:
                    running = False
        if event.type == GAME_UPDATE and not game.grid.game_over:
            game.move_piece("down")

    # RGB = Red, Green, Blue
    screen.fill((10, 10, 10))
    # TITLE
    screen.blit(
        title_surface, (((screen_width * 1.5) - title_surface.get_width()) // 2, 20)
    )
    # SCORE
    screen.blit(
        score_surface, (((screen_width * 1.5) - score_surface.get_width()) // 2, 120)
    )
    # SCORE NUMBER
    score_number_surface = normal_text_fond.render(str(game.score), True, (0, 255, 0))
    screen.blit(
        score_number_surface,
        (((screen_width * 1.5) - score_number_surface.get_width()) // 2, 160),
    )

    # TOP SCORES
    screen.blit(
        top_score_surface,
        (((screen_width * 1.5) - top_score_surface.get_width()) // 2, 230),
    )
    # TOP SCORES NUMBERS
    for i in range(len(scores)):
        screen.blit(
            normal_text_fond.render(str(scores[i]), True, (0, 255, 0)),
            (
                (
                    (screen_width * 1.5)
                    - normal_text_fond.render(
                        str(scores[i]), True, (0, 255, 0)
                    ).get_width()
                )
                // 2,
                270 + i * 40,
            ),
        )

    # NEXT PIECE
    screen.blit(
        next_piece_surface,
        (((screen_width * 1.5) - next_piece_surface.get_width()) // 2, 430),
    )
    # ACUTAL GAME SCREEN
    game.draw(screen)

    # GAME OVER
    if game.grid.game_over:
        pygame.draw.rect(screen, (10, 10, 10), game_over_rect)
        screen.blit(
            game_over_surface,
            ((screen_width - game_over_surface.get_width()) // 2, 200),
        )
        screen.blit(
            restart_or_quit_surface,
            ((screen_width - restart_or_quit_surface.get_width()) // 2, 300),
        )

    pygame.display.update()
    clock.tick(60)
