from game.organisms.animals.animal import Animal
from game.point import Point


class Wolf(Animal):
    def __init__(self, point: Point):
        super().__init__(9, 5, point)

    def get_symbol(self) -> str:
        return "W"