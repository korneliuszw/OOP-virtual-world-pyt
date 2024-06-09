from time import time
from tkinter.filedialog import askopenfile, asksaveasfile
import dearpygui.dearpygui as dbg

from game.world import World
from ui.board.base import BoardPaneHolder

class MainFrame():
    __boardPaneHolder: BoardPaneHolder
    __save_path = None
    __load_path = None
    __world: World
    __abilityStatus = None
    __keyboardManager = None

    
    def __init__(self, world: World, boardPaneHolder: BoardPaneHolder) -> None:
        self.__world = world
        self.__boardPaneHolder = boardPaneHolder
        with dbg.window(tag="Main frame"):
            self.__create()

    def __create(self):
        self.__createMenu()
        dbg.add_text("Hello World")
        dbg.delete_item("board_window")
        self.__boardPaneHolder.get().create()

    def __createMenu(self):
            with dbg.menu(label="Game"):
                dbg.add_menu_item(label="Save", callback=self.__save)
                dbg.add_menu_item(label="Load", callback=self.__load)

    def __save(self):
        default_name = f"{time()}.world"
        try:
            with asksaveasfile(initialfile=default_name, defaultextension=".world", filetypes=[("Game Save", ".world")]) as file:
                file.write("hello\n")
        except:
             pass
             

    def __load(self):
        try:
            with askopenfile(defaultextension=".world", filetypes=[("Game Save", ".world")]) as file:
                print(file.readlines())
        except:
            pass

    def __createContentPane():
        pass