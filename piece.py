import pygame


class Piece:
    def __init__(self, id, cell_size=30):
        self.id = id
        self.cell_size = cell_size
        self.rotation = 0
        self.cells = {}
        self.position_y = 0
        self.position_x = 0

    def move(self, direction, check_function, update_function):
        if direction == "down":
            self.position_y += 1
            if not check_function(self):
                self.position_y -= 1
                update_function()
        elif direction == "left":
            self.position_x -= 1
            if not check_function(self):
                self.position_x += 1
        elif direction == "right":
            self.position_x += 1
            if not check_function(self):
                self.position_x -= 1

    def rotate(self, check_function):
        self.rotation = (self.rotation + 1) % len(self.cells)
        if not check_function(self):
            self.rotation = (self.rotation - 1) % len(self.cells)

    def draw_shape(self, screeen):
        for cell in self.cells[self.rotation]:
            pygame.draw.rect(
                screeen,
                (0, 255, 0),
                (
                    (cell.x + self.position_x) * self.cell_size + 5,
                    (cell.y + self.position_y) * self.cell_size + 5,
                    self.cell_size - 5,
                    self.cell_size - 5,
                ),
                7,
            )
