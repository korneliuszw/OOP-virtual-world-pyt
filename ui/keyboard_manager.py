from asyncio import Event
from threading import Thread
from game.world import World
import dearpygui.dearpygui as dpg

task_interrupt_event = Event()


class KeyboardManager():
    __world: World
    __thread: Thread = None

    def __init__(self, world: World):
        self.__world = world
        with dpg.handler_registry():
            dpg.add_key_press_handler(dpg.mvKey_E, callback=self.__use_ability)
            dpg.add_key_press_handler(dpg.mvKey_Return, callback=self.__turn)

    def __move(self, _sender, data):
        key = data[0]
        print(key, data)
        pass

    def __use_ability(self):
        pass

    def __turn(self):
        if self.__thread != None and self.__thread.is_alive():
            return
        self.__thread = Thread(target=self.__world.turn)
        self.__thread.run()
        

    def set_world(self, world: World):
        self.__world = world
    
    def reset(self):
        if self.__thread != None and self.__thread.is_alive():
            task_interrupt_event.set()
            self.__thread.join()
            self.__thread = None
    
