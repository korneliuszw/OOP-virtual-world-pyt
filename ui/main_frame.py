from copy import deepcopy
import pickle
from time import time
from tkinter.filedialog import askopenfilename, asksaveasfilename
import dearpygui.dearpygui as dbg

from game.point import Point
from game.world import World
from ui.ability import create_ability_status
from ui.board.base import BoardPaneHolder
from ui.keyboard_manager import KeyboardManager

class MainFrame():
    __boardPaneHolder: BoardPaneHolder
    __world: World
    __keyboard: KeyboardManager

    
    def __init__(self, world: World, boardPaneHolder: BoardPaneHolder, keyboard) -> None:
        self.__world = world
        self.__boardPaneHolder = boardPaneHolder
        self.__keyboard = keyboard
        with dbg.window(tag="Main frame"):
            self.__create()

    def __create(self):
        self.__createMenu()
        create_ability_status()
        dbg.delete_item("board_window")
        self.__boardPaneHolder.get().create()

    def __createMenu(self):
            with dbg.menu(label="Game"):
                dbg.add_menu_item(label="Save", callback=self.__save)
                dbg.add_menu_item(label="Load", callback=self.__load)

    def __save(self):
        default_name = f"{time()}.world"
        try:
            path = asksaveasfilename(initialfile=default_name, defaultextension=".world", filetypes=[("Game Save", ".world")])
            with open(path, "w") as file:
                try:
                    self.__world.save(file)
                except Exception as e:
                    print(e)
                file.close()
        except:
             pass
             

    def __load(self):
        try:
            path = askopenfilename(defaultextension=".world", filetypes=[("Game Save", ".world")])
            with open(path, "r") as file:
                try:
                    self.__world.load(file)
                    self.__keyboard.set_world(self.__world)
                    self.__keyboard.reset()
                    self.__boardPaneHolder.get().change_world(self.__world)
                    self.__boardPaneHolder.get().create()
                    self.__boardPaneHolder.get().draw()
                except Exception as e:
                    print(e)
                file.close()

        except:
            pass