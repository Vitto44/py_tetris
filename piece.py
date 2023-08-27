import pygame


class Piece:
    def __init__(self, id, cell_size=30):
        self.id = id
        self.cell_size = cell_size
        self.rotation = 0
        self.cells = {}
        self.position_x = 0
        self.position_y = 0

    def move(self, direction):
        if direction == "down":
            self.position_x += 1
        elif direction == "left":
            self.position_y -= 1
        elif direction == "right":
            self.position_y += 1
        elif direction == "up":
            self.position_x -= 1

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
                    (cell.x + self.position_y) * self.cell_size + 5,
                    (cell.y + self.position_x) * self.cell_size + 5,
                    self.cell_size - 5,
                    self.cell_size - 5,
                ),
                7,
            )
