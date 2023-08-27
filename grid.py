import pygame


class Grid:
    def __init__(self, width=10, height=20, cell_size=30):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def is_valid(self, piece):
        for cell in piece.cells[piece.rotation]:
            x = cell.x + piece.position_y
            y = cell.y + piece.position_x
            if (
                x < 0
                or x >= self.width
                or y < 0
                or y >= self.height
                or self.grid[y][x] != 0
            ):
                return False
        return True

    def draw_grid(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(
                    screen,
                    (200, 200, 200),
                    (
                        j * self.cell_size + 5,
                        i * self.cell_size + 5,
                        self.cell_size - 5,
                        self.cell_size - 5,
                    ),
                    1,
                )
