from game.board.base import BoardSupplier
from game.point import Point


class SquareBoard(BoardSupplier):
    __width: int
    __height: int

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def get_new_position(self, current: Point, move: int) -> Point:
        if (move == 0):
            return Point(current.x - 1, current.y)
        elif (move == 1):
            return Point(current.x + 1, current.y)
        elif (move == 2):
            return Point(current.x, current.y - 1)
        elif (move == 3):
            return Point(current.x, current.y + 1)
        raise "Invalid move"
    
    def neighbours(self, ) -> int:
        return 4

    def is_legal_position(self, position: Point) -> bool:
        return position.x >= 0 and position.x < self.__width and position.y >= 0 and position.y < self.__height
        