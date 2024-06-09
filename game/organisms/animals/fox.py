from game.organisms.animals.animal import Animal
from game.point import Point
from game.world import World


class Fox(Animal):
    def __init__(self, position: Point):
        super().__init__(3, 7, position)

    def get_symbol(self) -> str:
        return "L"
    
    def _can_move_there(self, world: World, position: Point, skip_occupied: bool) -> bool:
        organism = world.get_organisms().get_entity_at(position)
        if organism != None and organism.get_atack() > self.get_atack():
            return False
        return super()._can_move_there(world, position, skip_occupied)