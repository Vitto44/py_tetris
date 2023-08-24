import pygame


class Grid:
    def __init__(self, x=10, y=20, cell_size=30):
        self.width = x
        self.height = y
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def draw_grid(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(
                    screen,
                    # if screen is 0 black, else green
                    (200, 200, 200),
                    (
                        j * self.cell_size + 5,
                        i * self.cell_size + 5,
                        self.cell_size - 5,
                        self.cell_size - 5,
                    ),
                    1 if self.grid[i][j] == 0 else 7,
                )
