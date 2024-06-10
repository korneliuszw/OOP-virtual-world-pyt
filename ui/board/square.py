from game.organisms.base import OrganismBase
from game.point import Point
from game.world import World
from ui.board.base import CELL_SIZE, BoardPaneBase
import dearpygui.dearpygui as dpg



class SquareBoardPane(BoardPaneBase):
    def __init__(self, world: World):
        super().__init__(world)

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
            dpg.add_text(default_value="", tag=tag_name+"move", color=(200, 100, 0), show=True, pos=(CELL_SIZE/2, 0))

    def _update_cell(self, organism: OrganismBase, cell_tag: str, move: int):
        text = organism.get_symbol() if organism != None else ""
        text_move = str(move) if move != None else ""
        dpg.configure_item(cell_tag + "move", default_value=text_move, show=(move != None))
        dpg.configure_item(cell_tag + "text", default_value=text)