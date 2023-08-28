from grid import Grid
from pieces import *
import random


class Game:
    def __init__(self):
        # self.clock = clock
        self.grid = Grid(10, 20, 30)
        self.game_over = False
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

    def get_piece(self):
        piece = Ipiece()
        return piece

    def draw(self, screen):
        self.grid.draw_grid(screen)
        self.current_piece.draw_shape(screen)

    def update_game_grid(self):
        self.grid.update_grid(self.current_piece)
        self.current_piece = self.next_piece
        self.next_piece = self.get_piece()

    def move_piece(self, direction):
        self.current_piece.move(direction, self.grid.is_valid, self.update_game_grid)
        if self.grid.full_grid:
            self.game_over = True

    def rotate_piece(self):
        self.current_piece.rotate(self.grid.is_valid)
