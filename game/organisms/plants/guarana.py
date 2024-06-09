from typing import Any
from game.organisms.base import OrganismBase
from game.organisms.plants.plant import Plant
from game.point import Point
from game.world import World


class Guarana(Plant):

    def __init__(self, point: Point) -> None:
        super().__init__(point)

    def _collide(self, world: World, collider: OrganismBase) -> bool:
        collider.set_attack(collider.get_atack() + 3)
        self.kill()
        # TODO: Log
        return True
    
    def get_symbol(self) -> str:
        return "G"