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
        player: Player = self.__world.get_player()
        player.move(self.__world, key)

    def __use_ability(self):
        player: Player = self.__world.get_player()
        player.activate_ability()
        pass

    __future: Future = None
    def __turn(self):
        try:
            if self.__world.get_player().is_waiting() and self.__future and not self.__future.done():
                return
            elif self.__future and self.__future.running() and not self.__world.get_player().is_waiting():
                task_interrupt_event.set()
            if self.__future:
                self.__future.result()
            task_interrupt_event.clear()
            self.__future = self.__executor.submit(self.__world.turn)
        except Exception as e:
            print(e)
        

    def set_world(self, world: World):
        self.__world = world
    
    def reset(self):
        task_interrupt_event.set()
        self.__executor.shutdown(cancel_futures=True)
        self.__executor = ThreadPoolExecutor(max_workers=1)
