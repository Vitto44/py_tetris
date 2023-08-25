import pygame


class Piece:
    def __init__(self, id, cell_size=30):
        self.id = id
        self.cell_size = cell_size
        self.rotation = 0
        self.cells = {}

    def move(self, direction):
        if direction == "down":
            for cell in self.cells[self.rotation]:
                cell[1] += 1
        elif direction == "left":
            for cell in self.cells[self.rotation]:
                cell[0] -= 1
        elif direction == "right":
            for cell in self.cells[self.rotation]:
                cell[0] += 1
        elif direction == "up":
            for cell in self.cells[self.rotation]:
                cell[1] -= 1

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.cells)

    def rotate_back(self):
        self.rotation = (self.rotation - 1) % len(self.cells)

    def draw_shape(self, screeen):
        for cell in self.cells[self.rotation]:
            pygame.draw.rect(
                screeen,
                (0, 255, 0),
                (
                    cell[0] * self.cell_size + 5,
                    cell[1] * self.cell_size + 5,
                    self.cell_size - 5,
                    self.cell_size - 5,
                ),
                7,
            )
