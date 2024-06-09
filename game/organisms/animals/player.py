from multiprocessing import Event
from time import sleep
from typing import Any
from game.organisms.animals.animal import Animal
from game.point import Point
from game.world import World
from ui.ability import show_ability_status

task_interrupt_event = Event()

ABILITY_DURATION = 5

class Ability:
    __cooldown_until = 0
    __available_until = 0
    __player: 'Player'

    def __init__(self, player):
        self.__player = player

    def is_available(self):
        return self.__available_until <= self.__player.get_age() and self.__cooldown_until <= self.__player.get_age()

    def is_activated(self):
        return self.__available_until > self.__player.get_age()
    
    def activate(self):
        if not self.is_available():
            return
        # TODO: Log?
        self.__available_until = self.__player.get_age() + ABILITY_DURATION
    
    def update(self, world: World):
        if not self.is_activated():
            return
        board = world.get_board()
        for x in range(0, board.neighbours()):
            neighbour = board.get_new_position(self.__player.get_position(), x)
            organisms = world.get_organisms().get_mapper()
            if neighbour in organisms:
                for organism in organisms[neighbour]:
                    organism.kill()
                    # TODO: Log?

    def update_timers(self):
        if self.__available_until != 0 and self.__available_until <= self.__player.get_age() and self.__available_until > self.__cooldown_until:
            # TODO: Log?
            self.__cooldown_until = self.__available_until + ABILITY_DURATION

class Player(Animal):
    __waiting = False
    __ability: 'Ability'
    __pending_move: Point = None

    def __init__(self, point: Point):
        super().__init__(5, 4, point)
        self.__ability = Ability(self)
    
    def get_symbol(self) -> str:
        return "P"
    
    def show_ability(self):
        show_ability_status(self.__ability)

    def act(self, world: World):
        self.__ability.update_timers()
        self.show_ability()
        self.__waiting = True
        world.get_board_pane().get().draw()
        while self.__pending_move is None:
            if task_interrupt_event.is_set():
                return
            sleep(0.1)
        self.__waiting = False
        self._moveThisOrganism(world, self.__pending_move)
        self.__pending_move = None
        self.__ability.update(world)

    def activate_ability(self):
        if self.__ability.is_available():
            self.__ability.activate()
            self.show_ability()

    def move(self, world: World, neighbour: int):
        self.__pending_move = world.get_board().get_new_position(self.get_position(), neighbour)

    def is_waiting(self):
        return self.is_waiting()
    