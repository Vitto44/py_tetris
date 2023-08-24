from grid import Grid
from pieces import *
import random


class Game:
    def __init__(self):
        # self.clock = clock
        self.grid = Grid(10, 20, 30)
        self.pieces = [Ipiece(), Jpiece(), Lpiece(), Spiece(), Tpiece()]
        self.current_piece = self.get_piece()
        self.next_piece = self.get_piece()

    def get_piece(self):
        piece = random.choice(self.pieces)
        return piece

    def draw(self, screen):
        self.grid.draw_grid(screen)
        self.current_piece.draw_shape(screen)
