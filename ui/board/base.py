from abc import ABC, abstractmethod
from typing import Dict

from game.board.base import BoardSupplier
from game.organisms.animals.player import Player
from game.organisms.base import OrganismBase
from game.organisms.dao import OrganismDAO
from game.point import Point
from game.world import World
import dearpygui.dearpygui as dpg

CELL_SIZE = 32

class BoardPaneBase(ABC):
    _organisms: OrganismDAO
    _width: int
    _height: int
    _boardSupplier: BoardSupplier
    _player: Player

    def __init__(self, world: World):
        self.change_world(world)

    def cell_name(self, point: Point):
        return f"cell-{point.x}-{point.y}"

    @abstractmethod
    def _create_cell(self, position: Point):
        pass
    
    @abstractmethod
    # MUST handle organism == None, clear text 
    def _update_cell(self, organism: OrganismBase, cell_tag: str, move: int):
        pass

    def change_world(self, world: World):
        self._width = world.get_width()
        self._height = world.get_height()
        self._organisms = world.get_organisms()
        self._boardSupplier = world.get_board()
        self._player = world.get_player()
        self.previous_list = []

    @abstractmethod
    def _get_all_points(self) -> list[Point]:
        pass

    def __get_player_neighbours(self) -> Dict[Point, int]:
        neighbours = {}
        if not self._player.is_waiting() or not self._player.is_alive():
            return neighbours
        for x in range(0, self._boardSupplier.neighbours()):
            neighbour = self._boardSupplier.get_new_position(self._player.get_position(), x)
            if neighbour is not None:
                neighbours[neighbour] = x
        return neighbours

    def create(self):
        try:
            dpg.delete_item("board_window")
        except Exception as e:
            print(e)
            pass

        try:
            with dpg.child_window(width=CELL_SIZE*(self._width+1), height=CELL_SIZE*(self._height+1),show=True,tag="board_window", horizontal_scrollbar=True, parent="Main frame"):
                for point in self._get_all_points():
                    self._create_cell(point)
                    # TODO: PLayer move
        except Exception as e:
            print(e)
            pass

    previous_list = []
    def draw(self):
        for previous in self.previous_list:
            cell_tag = self.cell_name(previous)
            self._update_cell(None, cell_tag, None)
        self.previous_list.clear()
        neighbours = self.__get_player_neighbours()
        for organismList in self._organisms.get_all():
            alive_list = list(filter(lambda x: x.is_alive(), organismList))
            if len(alive_list) == 0 :
                continue
            organism = alive_list[0]
            position = organism.get_position()
            if not self._boardSupplier.is_legal_position(position):
                continue
            cell_tag = self.cell_name(position)
            move = neighbours[position] if position in neighbours else None
            if move:
                del neighbours[position]
            self._update_cell(organism, cell_tag, move)
            self.previous_list.append(organism.get_position())

        for point in neighbours.keys():
            if not self._boardSupplier.is_legal_position(point):
                continue
            self._update_cell(None, self.cell_name(point), neighbours[point])
            self.previous_list.append(point)

class BoardPaneHolder:
    __pane: BoardPaneBase

    def get(self):
        return self.__pane
    
    def set(self, pane: BoardPaneBase):
        self.__pane = pane

    def __init__(self, pane: BoardPaneBase) -> None:
        self.__pane = pane
