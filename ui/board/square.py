from game.organisms.base import OrganismBase
from game.point import Point
from game.world import World
from ui.board.base import CELL_SIZE, BoardPaneBase
import dearpygui.dearpygui as dpg



class SquareBoardPane(BoardPaneBase):
    def __init__(self, world: World, width: int, height: int):
        super().__init__(world, width, height)

    def _get_all_points(self) -> list[Point]:
        points = []
        for x in range(0, self._width):
            for y in range(0, self._height):
                points.append(Point(x, y))

        return points
    
    def _create_cell(self, position: Point):
        tag_name = self.cell_name(position)
        with dpg.child_window(width=CELL_SIZE, height=CELL_SIZE, show=True, border=True, tag=tag_name, pos=(position.x * CELL_SIZE, position.y * CELL_SIZE), no_scrollbar=True):
            dpg.add_text(default_value="", tag=tag_name+"text")

    def _update_cell(self, organism: OrganismBase, cell_tag: str):
        text = organism.get_symbol() if organism != None else ""
        dpg.configure_item(cell_tag + "text", default_value=text)