from copy import deepcopy
from random import randint
from game.organisms.base import OrganismBase
from game.point import Point
from game.world import World


MINIMUM_SPAWN_AGE = 5

class Plant(OrganismBase):
    _spawnRateUpperBound = 8
    
    def __init__(self, point: Point) -> None:
        super().__init__(0, 0, point)

    def act(self, world: World):
        rng = randint(1, self._spawnRateUpperBound)
        if self.get_age() < MINIMUM_SPAWN_AGE or rng != 1:
            return
        position = self.generate_random_legal_position(world, True)
        if position == self.get_position():
            return
        child = deepcopy(self);
        child.set_age(0)
        child.set_position(position)
        # TODO: Log
        world.get_organisms().spawn(child)