from typing import Any
from game.organisms.animals.animal import Animal
from game.organisms.animals.cybersheep import Cybersheep
from game.organisms.base import OrganismBase
from game.organisms.plants.plant import Plant
from game.point import Point
from game.world import World


class SosnowskyWeed(Plant):
    def __init__(self, point: Point) -> None:
        super().__init__(point)

    def get_symbol(self) -> str:
        return "B"
    
    def _collide(self, _world: World, collider: OrganismBase) -> bool:
        self.kill()
        if not isinstance(collider, Cybersheep):
            collider.kill()
            # TODO: Log
            print(f"Barsz zabija po zjedzeniu {collider.get_symbol()}")
        return True
    
    def act(self, world: World):
        board = world.get_board()
        for x in range(0, board.neighbours()):
            neighbour = board.get_new_position(self.get_position(), x )
            if neighbour is None: return
            organism = world.get_organisms().get_entity_at(neighbour)
            if isinstance(organism, Animal) and not isinstance(organism, Cybersheep):
                organism.kill()
                # TODO: Log
                print(f"Barsz zabija obok {organism.get_symbol}")