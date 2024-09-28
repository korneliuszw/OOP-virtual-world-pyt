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
            point =  Point(current.x - 1, current.y)
        elif (move == 1):
            point = Point(current.x + 1, current.y)
        elif (move == 2):
            point = Point(current.x, current.y - 1)
        elif (move == 3):
            point = Point(current.x, current.y + 1)
        if point is None:
            raise "Invalid move"
        if self.is_legal_position(point):
            return point
    
    def neighbours(self) -> int:
        return 4

    def is_legal_position(self, position: Point) -> bool:
        return position.x >= 0 and position.x < self.__width and position.y >= 0 and position.y < self.__height
        