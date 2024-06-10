from abc import ABC, abstractmethod
from random import randint
from typing import Any

from game.point import Point

NON_MOVABLE_ORGANISM = -1

class OrganismBase(ABC):
    __alive = True
    __position: Point = None
    __agressiveness: int = 0
    __age: int = 0
    __attack: int = 0
    __id: int = 0

    def __init__(self, attack: int, aggressiveness: int, point: Point) -> None:
        super().__init__()
        self.__attack = attack
        self.__agressiveness = aggressiveness
        self.__position = point

    def kill(self):
        self.__alive = False

    def end_turn(self):
        self.__age += 1

    def _moveThisOrganism(self, world, new_position: Point):
        if not world.get_board().is_legal_position(new_position):
            return
        colidee = world.get_organisms().get_entity_at(new_position)
        old_position = Point(self.__position.x, self.__position.y)
        self.__position = new_position
        world.get_organisms().move_organism(self, old_position)
        if colidee != None and colidee != self:
            if not colidee._collide(world, self):
                new_point = Point(self.__position.x, self.__position.y)
                self.__position = old_position
                world.get_organisms().move_organism(self, new_point)
        if self.__alive:
            # TODO: Log
            pass

    def _can_move_there(self, world, position: Point, skip_occupied: bool) -> bool:
        return not skip_occupied or world.get_organisms().get_entity_at(position) == None

    def generate_random_legal_position(self, world, skip_occupied: bool) -> Point:
        legal_positions = []
        board = world.get_board()
        for x in range(0, board.neighbours()):
            new_position = board.get_new_position(self.__position, x)
            if board.is_legal_position(new_position) and self._can_move_there(world, new_position, skip_occupied):
                legal_positions.append(new_position)
        if len(legal_positions) == 0:
            return self.__position
        random = randint(0, len(legal_positions) - 1)
        return legal_positions[random]
    
    def _collide(self, world, collider: 'OrganismBase') -> bool:
        # TODO: Log
        print(f"{self.get_symbol()} zderza sie z {collider.get_symbol()}")
        if collider.__attack > self.__attack:
            self.kill()
        else:
            collider.kill()
        return True

    def get_position(self) -> Point:
        return self.__position
    
    def get_atack(self) -> int:
        return self.__attack
    
    def get_age(self) -> int:
        return self.__age
    
    def get_aggressivness(self) -> int:
        return self.__agressiveness
    
    def is_alive(self) -> bool:
        return self.__alive
    
    def set_id(self, id: int):
        self.__id = id

    def set_age(self, age: int):
        self.__age = age

    def set_position(self, position: Point):
        self.__position = position
    
    def set_attack(self, attack: int):
        self.__attack = attack

    @abstractmethod
    def get_symbol(self) -> str:
        pass

    @abstractmethod
    def act(self, world):
        pass

    def __lt__(self, other: 'OrganismBase'):
        if self.get_aggressivness() == NON_MOVABLE_ORGANISM and other.get_aggressivness() != NON_MOVABLE_ORGANISM:
            return True
        elif other.get_aggressivness() == NON_MOVABLE_ORGANISM and self.get_aggressivness() != NON_MOVABLE_ORGANISM:
            return False
        elif self.get_aggressivness() == other.get_aggressivness():
            return True if self.get_age() < other.get_age() else False
        return True if self.get_aggressivness() < other.get_aggressivness() else False
    