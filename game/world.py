from io import FileIO
from traceback import format_exc, print_stack
from game.board.base import BoardSupplier
from heapq import heappush, heappop
from game.board.square import SquareBoard
from game.point import Point
from game.organisms.dao import OrganismDAO
from game.organisms.base import OrganismBase

class World:
    __width : int
    __height: int
    __action_queue: list['OrganismBase'] = []
    __organisms: OrganismDAO = OrganismDAO()
    __boardSuplier: BoardSupplier
    __player: 'OrganismBase'
    __board_pane_holder = None

    def __init__(self, width: int, height: int, boardSupplier: BoardSupplier, player: OrganismBase):
        self.__height = height
        self.__width = width
        self.__boardSuplier = boardSupplier
        self.__player = player

    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height
    
    def get_organisms(self) -> OrganismDAO:
        return self.__organisms
    
    def get_board(self) -> BoardSupplier:
        return self.__boardSuplier
    
    def get_board_pane(self):
        return self.__board_pane_holder

    def set_board_pane(self, board_pane_holder):
        self.__board_pane_holder = board_pane_holder

    def get_player(self):
        return self.__player
    
    def __act_turn(self):
        while (len(self.__action_queue) > 0):
            organism = heappop(self.__action_queue)
            if organism.get_symbol() == "P":
                self.__player = organism
            if organism.is_alive():
                organism.act(self)

    def __end_turn(self):
        mapper = self.__organisms.get_mapper()
        keys = list(mapper.keys())
        for key in keys:
            liste = list(filter(lambda x: x.is_alive(), mapper.get(key)))
            for item in liste:
                item.end_turn()
            if len(liste) == 0:
                del mapper[key]
    
    def turn(self):
        print('turn')
        self.__action_queue = []
        for list in self.__organisms.get_all():
            for organism in list:
                if organism.is_alive():
                    heappush(self.__action_queue, organism)
        self.__act_turn()
        self.__end_turn()
        print('finished')
        self.__board_pane_holder.get().draw()

    def save(self, file: FileIO):
        file.write(f"{self.get_height()}\n")
        file.write(f"{self.get_width()} \n")
        from game.organisms.animals.player import Player, Ability
        for organism_list in self.__organisms.get_all():
            for organism in organism_list:
                file.write(organism.get_symbol() + " ")
                file.write(f"{organism.get_position().x} {organism.get_position().y} ")
                file.write(f"{organism.get_age()} ")
                file.write(f"{organism.get_atack()}")
                if isinstance(organism, Player):
                    ability: Ability = organism.get_ability()
                    file.write(f" {ability._cooldown_until} {ability._available_until}")
                file.write("\n")
    
    def load(self, file: FileIO):
        height = int(file.readline().strip())
        width = int(file.readline().strip())
        from game.organisms.animals.antelope import Antelope
        from game.organisms.animals.cybersheep import Cybersheep
        from game.organisms.animals.fox import Fox
        from game.organisms.animals.player import Ability, Player
        from game.organisms.animals.sheep import Sheep
        from game.organisms.animals.wolf import Wolf
        from game.organisms.animals.turtle import Turtle
        from game.organisms.plants.belladonna import Belladona
        from game.organisms.plants.dandelion import Dandelion
        from game.organisms.plants.grass import Grass
        from game.organisms.plants.guarana import Guarana
        from game.organisms.plants.sosnowsky_weed import SosnowskyWeed
        dao = OrganismDAO()
        for line in file.readlines():
            line = line.strip()
            infos = line.split(" ")
            point = Point(int(infos[1]), int(infos[2]))
            age = int(infos[3])
            attack = int(infos[4])
            match infos[0]:
                case "A":
                    organism = Antelope(point)
                case "L":
                    organism = Fox(point)
                case "O":
                    organism = Sheep(point)
                case "CO":
                    organism = Cybersheep(point)
                case "Z":
                    organism = Turtle(point)
                case "W":
                    organism = Wolf(point)
                case "P":
                    self.__player = organism = Player(point)
                    ability = Ability(organism)
                    ability._cooldown_until = int(infos[5])
                    ability._available_until = int(infos[6])
                    organism.set_ability(ability)
                case "B":
                    organism = SosnowskyWeed(point)
                case "G":
                    organism = Guarana(point)
                case  "T":
                    organism = Grass(point)
                case "J":
                    organism = Belladona(point)
                case "M":
                    organism = Dandelion(point)
            organism.set_age(age)
            organism.set_attack(attack)
            dao.spawn(organism)
        self.__organisms = dao
        self.__height = height
        self.__width = width
        self.__boardSuplier = SquareBoard(width, height)