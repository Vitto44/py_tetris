from piece import Piece
from position import Position


class Lpiece(Piece):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            0: [Position(4, 2), Position(5, 0), Position(5, 1), Position(5, 2)],
            1: [Position(4, 1), Position(5, 1), Position(6, 1), Position(6, 2)],
            2: [Position(5, 0), Position(5, 1), Position(5, 2), Position(6, 0)],
            3: [Position(4, 0), Position(4, 1), Position(5, 1), Position(6, 1)],
        }


class Jpiece(Piece):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            0: [Position(4, 0), Position(5, 0), Position(5, 1), Position(5, 2)],
            1: [Position(4, 1), Position(4, 2), Position(5, 1), Position(6, 1)],
            2: [Position(5, 0), Position(5, 1), Position(5, 2), Position(6, 2)],
            3: [Position(4, 1), Position(5, 1), Position(6, 0), Position(6, 1)],
        }


class Ipiece(Piece):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [Position(5, 0), Position(5, 1), Position(5, 2), Position(5, 3)],
            1: [Position(4, 2), Position(5, 2), Position(6, 2), Position(7, 2)],
            2: [Position(6, 0), Position(6, 1), Position(6, 2), Position(6, 3)],
            3: [Position(4, 1), Position(5, 1), Position(6, 1), Position(7, 1)],
        }


class Opiece(Piece):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            0: [Position(4, 0), Position(4, 1), Position(5, 0), Position(5, 1)]
        }


class Spiece(Piece):
    def __init__(self):
        super().__init__(id=5)
        self.cells = {
            0: [Position(4, 1), Position(4, 2), Position(5, 0), Position(5, 1)],
            1: [Position(4, 1), Position(5, 1), Position(5, 2), Position(6, 2)],
            2: [Position(5, 1), Position(5, 2), Position(6, 0), Position(6, 1)],
            3: [Position(4, 0), Position(5, 0), Position(5, 1), Position(6, 1)],
        }


class Tpiece(Piece):
    def __init__(self):
        super().__init__(id=6)
        self.cells = {
            0: [Position(4, 1), Position(5, 0), Position(5, 1), Position(5, 2)],
            1: [Position(4, 1), Position(5, 1), Position(5, 2), Position(6, 1)],
            2: [Position(5, 0), Position(5, 1), Position(5, 2), Position(6, 1)],
            3: [Position(4, 1), Position(5, 0), Position(5, 1), Position(6, 1)],
        }


class Zpiece(Piece):
    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            0: [Position(4, 0), Position(4, 1), Position(5, 1), Position(5, 2)],
            1: [Position(4, 2), Position(5, 1), Position(5, 2), Position(6, 1)],
            2: [Position(5, 0), Position(5, 1), Position(6, 1), Position(6, 2)],
            3: [Position(4, 1), Position(5, 0), Position(5, 1), Position(6, 0)],
        }
