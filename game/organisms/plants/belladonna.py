from typing import Any
from game.organisms.base import OrganismBase
from game.organisms.plants.plant import Plant
from game.point import Point
from game.world import World


class Belladona(Plant):
    def __init__(self, point: Point) -> None:
        super().__init__(point)
    def get_symbol(self) -> str:
        return "J"
    
    def _collide(self, world: World, collider: OrganismBase) -> bool:
        if isinstance(collider, Plant):
            return True
        collider.kill()
        self.kill()
        # TODO: Log
        return True