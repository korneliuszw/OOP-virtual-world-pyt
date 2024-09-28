from queue import SimpleQueue
from typing import Dict
from game.organisms.animals.sheep import Sheep
from game.point import Point
from game.world import World


class Cybersheep(Sheep):
    __current_route = []

    def __init__(self, point: Point):
        super().__init__(point, 11, 4)

    def __find_weed(self, world: World):
        queue = SimpleQueue()
        queue.put(self.get_position())
        board = world.get_board()
        marked: Dict[Point, Point] = {}
        # BFS to locate closest weed and mark a route to it
        while not queue.empty():
            current = queue.get()
            for x in range(0, board.neighbours()):
                neighbour = board.get_new_position(current, x)
                if neighbour is None or neighbour in marked:
                    continue
                marked[neighbour] = current
                queue.put(neighbour)
                organism = world.get_organisms().get_entity_at(neighbour, "B")
                if organism == None:
                    continue
                # We found weed so mark a route to it
                route_element = neighbour
                while route_element != self.get_position():
                    self.__current_route.append(route_element)
                    route_element = marked[route_element]
                return
    def act(self, world: World):
        if len(self.__current_route) == 0:
            self.__find_weed(world)
            if len(self.__current_route) == 0:
                return super().act(world)
        position = self.__current_route.pop()
        self._moveThisOrganism(world, position)

    def get_symbol(self) -> str:
        return "CO"