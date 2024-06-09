from copy import deepcopy
from random import randint
from typing import Any
from game.organisms.animals.animal import Animal
from game.point import Point
from game.world import World


class Antelope(Animal):

    def __init__(self,point: Point):
        super().__init__(4, 4, point)

    def get_symbol(self) -> str:
        return "A"
    
    def act(self, world: World):

        current = deepcopy(self.get_position())
        self.set_position(self.generate_random_legal_position(world, False))
        new_position = self.generate_random_legal_position(world, False)
        self.set_position(current)
        self._moveThisOrganism(world, new_position)

    def _collide(self, world: World, collider: Any) -> bool:
        rng = randint(0, 1)
        if rng == 1:
            pos = self.generate_random_legal_position(world, True)
            if pos != self.get_position():
                # TODO: log
                self._moveThisOrganism(world, pos)
                return True
        return super()._collide(world, collider)