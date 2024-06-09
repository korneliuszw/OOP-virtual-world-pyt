from abc import ABC
from copy import deepcopy
from typing import Any

from game.organisms.base import OrganismBase
from game.point import Point
from game.world import World

MINIMUM_AGE_TO_MATE = 5

class Animal(OrganismBase, ABC):
    __did_mate = False

    def __init__(self, attack: int, aggressiveness: int, point: Point):
        super().__init__(attack, aggressiveness, point)

    def __mate(self, world: World, other: Any):
        position = self.generate_random_legal_position(world, True)
        if position == self.get_position() or self.__did_mate:
            return
        child: OrganismBase = deepcopy(other)
        child.set_age(0)
        child.set_position(position)
        # TODO: Log
        world.get_organisms().spawn(child)
        self.__did_mate = True
    
    def act(self, world: World):
        self._moveThisOrganism(world, self.generate_random_legal_position(world, False))

    def end_turn(self):
        self.__did_mate = False
        return super().end_turn()
    
    def _collide(self, world: World, collider: Any) -> bool:
        if collider.get_symbol() == self.get_symbol() and collider.get_age() >= MINIMUM_AGE_TO_MATE and self.get_age() >= MINIMUM_AGE_TO_MATE:
            self.__mate(world, collider)
            return True
        return super()._collide(world, collider)