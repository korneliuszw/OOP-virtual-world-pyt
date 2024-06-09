from game.organisms.plants.plant import Plant
from game.point import Point


class Grass(Plant):
    def __init__(self, point: Point) -> None:
        super().__init__(point)

    def get_symbol(self) -> str:
        return "T"