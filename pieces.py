from piece import Piece


class Opiece(Piece):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            0: [[4, 0], [4, 1], [5, 0], [5, 1]],
        }


class Ipiece(Piece):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            0: [[5, 0], [5, 1], [5, 2], [5, 3]],
            1: [[4, 1], [5, 1], [6, 1], [7, 1]],
            2: [[6, 0], [6, 1], [6, 2], [6, 3]],
            3: [[4, 2], [5, 2], [6, 2], [7, 2]],
        }


class Lpiece(Piece):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [[4, 2], [5, 0], [5, 1], [5, 2]],
            1: [[4, 1], [5, 1], [6, 1], [6, 2]],
            2: [[5, 0], [5, 1], [5, 2], [6, 0]],
            3: [[4, 0], [4, 1], [5, 1], [6, 1]],
        }


class Jpiece(Piece):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            0: [[4, 0], [5, 0], [5, 1], [5, 2]],
            1: [[4, 1], [4, 2], [5, 1], [6, 1]],
            2: [[5, 0], [5, 1], [5, 2], [6, 2]],
            3: [[4, 1], [5, 1], [6, 0], [6, 1]],
        }


class Spiece(Piece):
    def __init__(self):
        super().__init__(id=5)
        self.cells = {
            0: [[4, 1], [4, 2], [5, 0], [5, 1]],
            1: [[4, 1], [5, 1], [5, 2], [6, 2]],
            2: [[5, 1], [5, 2], [6, 0], [6, 1]],
            3: [[4, 0], [5, 0], [5, 1], [6, 1]],
        }


class Tpiece(Piece):
    def __init__(self):
        super().__init__(id=6)
        self.cells = {
            0: [[4, 1], [5, 1], [5, 2], [6, 1]],
            1: [[4, 1], [5, 0], [5, 1], [5, 2]],
            2: [[4, 1], [5, 0], [5, 1], [6, 1]],
            3: [[5, 0], [5, 1], [5, 2], [6, 1]],
        }


class Zpiece(Piece):
    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            0: [[4, 0], [4, 1], [5, 1], [5, 2]],
            1: [[4, 2], [5, 1], [5, 2], [6, 1]],
            2: [[5, 0], [5, 1], [6, 1], [6, 2]],
            3: [[4, 1], [5, 0], [5, 1], [6, 0]],
        }
