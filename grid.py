import pygame


class Grid:
    def __init__(self, width=10, height=20, cell_size=30):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.game_over = False
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def is_valid(self, piece):
        for cell in piece.cells[piece.rotation]:
            x = cell.x + piece.position_x
            y = cell.y + piece.position_y
            # check for full grid
            if self.grid[0][x] != 0:
                self.game_over = True
            if (
                x < 0
                or x >= self.width
                or y < 0
                or y >= self.height
                or self.grid[y][x] != 0
            ):
                return False
        return True

    def update_grid(self, piece):
        for cell in piece.cells[piece.rotation]:
            x = cell.x + piece.position_x
            y = cell.y + piece.position_y
            self.grid[y][x] = piece.id
        # RESET movement back to 0.
        # If Not the new piece that is of the same type as the previous piece will have same position as the previous piece
        piece.position_y = 0
        piece.position_x = 0

    def check_grid_for_points(self):
        lines_to_remove = []
        for i in range(self.height):
            if 0 not in self.grid[i]:
                lines_to_remove.append(i)
        self.remove_lines(lines_to_remove)
        return len(lines_to_remove)

    def remove_lines(self, lines_to_remove):
        for index in lines_to_remove:
            self.grid.pop(index)
            self.grid.insert(0, [0 for _ in range(self.width)])

    def draw_grid(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(
                    screen,
                    (200, 200, 200) if self.grid[i][j] == 0 else (255, 255, 255),
                    (
                        j * self.cell_size + 5,
                        i * self.cell_size + 5,
                        self.cell_size - 5,
                        self.cell_size - 5,
                    ),
                    1 if self.grid[i][j] == 0 else 7,
                )
