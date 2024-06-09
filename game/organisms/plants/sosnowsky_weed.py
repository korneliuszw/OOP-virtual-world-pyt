from typing import Any
from game.organisms.animals.animal import Animal
from game.organisms.base import OrganismBase
from game.organisms.plants.plant import Plant
from game.point import Point
from game.world import World


class SosnowskyWeed(Plant):
    def __init__(self, point: Point) -> None:
        super().__init__(point)

    def get_symbol(self) -> str:
        return "B"
    
    def _collide(self, world: World, collider: OrganismBase) -> bool:
        collider.kill()
        self.kill()
        # TODO: Log
        return True
    
    def act(self, world: World):
        board = world.get_board()
        for x in range(0, board.neighbours()):
            neighbour = board.get_new_position(self.get_position(), x )
            organism = world.get_organisms().get_entity_at(neighbour)
            if isinstance(organism, Animal):
                organism.kill()
                # TODO: Log