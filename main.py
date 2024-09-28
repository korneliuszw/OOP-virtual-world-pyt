from tkinter.simpledialog import askinteger
import dearpygui.dearpygui as dpg

from game.factory import createWorld
from ui.board.base import BoardPaneHolder
from ui.board.square import SquareBoardPane
from ui.keyboard_manager import KeyboardManager
from ui.main_frame import MainFrame

def __main__():
    dpg.create_context()
    dpg.create_viewport(title="Wirtualny swiat 198349", width=800, height=600)
    width = askinteger("Szerokosc", "Podaj szerokosc > 0")
    height = askinteger("Wysokosc", "Podaj wysokosc > 0")
    world = createWorld(width, height)
    keyboard = KeyboardManager(world)
    board_pane = BoardPaneHolder(SquareBoardPane(world))
    main_frame = MainFrame(world, board_pane, keyboard)
    world.set_board_pane(board_pane)
    board_pane.get().draw()
    dpg.set_primary_window("Main frame", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()

    try:
        dpg.start_dearpygui()

    except KeyboardInterrupt:
        keyboard.reset()
        exit(0)

    dpg.destroy_context()
__main__()