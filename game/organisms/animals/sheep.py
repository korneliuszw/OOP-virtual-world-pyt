from game.organisms.animals.animal import Animal
from game.point import Point


class Sheep(Animal):
    def __init__(self, point: Point):
        super().__init__(4, 4, point)

    def get_symbol(self) -> str:
        return "O"