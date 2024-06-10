from game.organisms.animals.animal import Animal
from game.point import Point


class Sheep(Animal):
    def __init__(self, point: Point, attack = 4, aggresiv = 4):
        super().__init__(attack, aggresiv, point)

    def get_symbol(self) -> str:
        return "O"