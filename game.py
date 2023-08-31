from grid import Grid
from pieces import *
import random
import pygame


class Game:
    def __init__(self):
        self.grid = Grid(10, 20, 30)
        self.score = 0
        self.pieces = [
            Ipiece(),
            Jpiece(),
            Lpiece(),
            Opiece(),
            Spiece(),
            Tpiece(),
            Zpiece(),
        ]
        self.current_piece = self.get_piece()
        self.next_piece = self.get_piece()
        self.clear_lines_sound = pygame.mixer.Sound("audio/pixel_effect.mp3")
        self.game_over_sound = pygame.mixer.Sound("audio/game_over.mp3")
        pygame.mixer.music.load("audio/theme_song.mp3")
        pygame.mixer.music.play(-1)

    def get_piece(self):
        # choose random and pop out of list
        if (len(self.pieces)) == 0:
            self.pieces = [
                Ipiece(),
                Jpiece(),
                Lpiece(),
                Opiece(),
                Spiece(),
                Tpiece(),
                Zpiece(),
            ]
        piece = random.choice(self.pieces)
        self.pieces.remove(piece)
        return piece

    def reset(self):
        self.grid = Grid(10, 20, 30)
        self.score = 0
        self.current_piece = self.get_piece()
        self.next_piece = self.get_piece()
        # if they are the same piece, get a new one
        if self.current_piece == self.next_piece:
            self.next_piece = self.get_piece()
        pygame.mixer.music.play(-1)

    def draw(self, screen):
        self.grid.draw_grid(screen)
        self.current_piece.draw_shape(screen)
        self.next_piece.draw_shape(screen, next_piece=True)

    def update_game_grid(self):
        self.grid.update_grid(self.current_piece)
        lines_removed = self.grid.check_grid_for_points()
        self.current_piece = self.next_piece
        self.next_piece = self.get_piece()
        if lines_removed:
            self.clear_lines_sound.play()
            self.update_score(lines_removed)

    def update_score(self, lines_removed):
        if lines_removed == 1:
            self.score += 100
        elif lines_removed == 2:
            self.score += 300
        elif lines_removed == 3:
            self.score += 500
        elif lines_removed == 4:
            self.score += 800
        pygame.time.set_timer(pygame.USEREVENT, 600 - (self.score // 10))

    def move_piece(self, direction):
        self.current_piece.move(direction, self.grid.is_valid, self.update_game_grid)
        if self.grid.game_over:
            self.game_over_sound.play()
            pygame.mixer.music.stop()

    def rotate_piece(self):
        self.current_piece.rotate(self.grid.is_valid)
