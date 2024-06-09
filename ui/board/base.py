from abc import ABC, abstractmethod

from game.board.base import BoardSupplier
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

    def __init__(self, world: World, width: int, height: int):
        self._organisms = world.get_organisms()
        self._height = height
        self._width = width

    def _get_organism_at(self, point: Point):
        real_point = self.translate_point(point)
        return self._organisms.get_entity_at(real_point)
    
    def cell_name(self, point: Point):
        return f"cell-{point.x}-{point.y}"

    @abstractmethod
    def _create_cell(self, position: Point):
        pass
    
    @abstractmethod
    # MUST handle organism == None, clear text 
    def _update_cell(self, organism: OrganismBase, cell_tag: str):
        pass

    def change_world(self, world: World):
        self._width = world.get_width()
        self._height = world.get_height()
        self._organisms = world.get_organisms()

    @abstractmethod
    def _get_all_points(self) -> list[Point]:
        pass

    def __get_player_neighbours(self):
        pass

    def create(self):
        with dpg.child_window(width=CELL_SIZE*(self._width+1), height=CELL_SIZE*(self._height+1),show=True,tag="board_window", horizontal_scrollbar=True):
            for point in self._get_all_points():
                self._create_cell(point)
                # TODO: PLayer move
    previous_list = []
    def draw(self):
        for previous in self.previous_list:
            cell_tag = self.cell_name(previous)
            self._update_cell(None, cell_tag)
        self.previous_list.clear()
        for organismList in self._organisms.get_all():
            organism = organismList[0]
            cell_tag = self.cell_name(organism.get_position())
            self._update_cell(organism, cell_tag)
            self.previous_list.append(organism.get_position())

class BoardPaneHolder:
    __pane: BoardPaneBase

    def get(self):
        return self.__pane
    
    def set(self, pane: BoardPaneBase):
        self.__pane = pane

    def __init__(self, pane: BoardPaneBase) -> None:
        self.__pane = pane
