from concurrent.futures import Future, ThreadPoolExecutor
from game.organisms.animals.player import Player, task_interrupt_event
from game.world import World
import dearpygui.dearpygui as dpg



class KeyboardManager():
    __world: World
    __executor: ThreadPoolExecutor

    def __init__(self, world: World):
        self.__world = world
        self.__executor = ThreadPoolExecutor(max_workers=1)
        with dpg.handler_registry():
            dpg.add_key_press_handler(dpg.mvKey_E, callback=self.__use_ability)
            dpg.add_key_press_handler(dpg.mvKey_0, callback=self.__move)
            dpg.add_key_press_handler(dpg.mvKey_1, callback=self.__move)
            dpg.add_key_press_handler(dpg.mvKey_2, callback=self.__move)
            dpg.add_key_press_handler(dpg.mvKey_3, callback=self.__move)
            dpg.add_key_press_handler(dpg.mvKey_Return, callback=self.__turn)

    def __move(self, _sender, data):
        key = data - dpg.mvKey_0
        print(key)
        player: Player = self.__world.get_player()
        player.move(self.__world, key)
        pass

    def __use_ability(self):
        player: Player = self.__world.get_player()
        player.activate_ability()
        pass

    __future: Future = None
    def __turn(self):
        if self.__future != None and self.__future.running():
            return
        self.__future = self.__executor.submit(self.__world.turn)
        

    def set_world(self, world: World):
        self.__world = world
    
    def reset(self):
        task_interrupt_event.set()
        self.__executor.shutdown(cancel_futures=True)
        task_interrupt_event.clear()
