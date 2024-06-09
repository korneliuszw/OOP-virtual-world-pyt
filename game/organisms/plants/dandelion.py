from game.organisms.plants.plant import Plant
from game.point import Point
from game.world import World


class Dandelion(Plant):

    def __init__(self, point: Point) -> None:
        super().__init__(point)

    def get_symbol(self) -> str:
        return "M"
    
    def act(self, world: World):
        super().act(world)
        super().act(world)
        super().act(world)