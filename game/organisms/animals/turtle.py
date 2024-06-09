from random import randint
from typing import Any
from game.organisms.animals.animal import Animal
from game.organisms.base import OrganismBase
from game.point import Point
from game.world import World


class Turtle(Animal):
    def __init__(self, point: Point):
        super().__init__(2, 1, point)
    
    def get_symbol(self) -> str:
        return "Z"
    
    def _collide(self, world: World, collider: OrganismBase) -> bool:
        if collider.get_atack() < 5:
            return False
        return super()._collide(world, collider)
    
    def act(self, world: World):
        rng = randint(1, 4)
        # 25% to move
        if rng == 2:
            super().act(world)