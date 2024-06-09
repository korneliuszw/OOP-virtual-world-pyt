from game.board.base import BoardSupplier
from heapq import heappush, heappop


class World:
    from game.organisms.base import OrganismBase
    from game.organisms.dao import OrganismDAO
    __width : int
    __height: int
    __action_queue: list['OrganismBase'] = []
    __organisms: OrganismDAO = OrganismDAO()
    __boardSuplier: BoardSupplier
    __player: 'OrganismBase'
    __board_pane_holder = None

    def __init__(self, width: int, height: int, boardSupplier: BoardSupplier, player: OrganismBase):
        self.__height = height
        self.__width = width
        self.__boardSuplier = boardSupplier
        self.__player = player

    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height
    
    def get_organisms(self) -> OrganismDAO:
        return self.__organisms
    
    def get_board(self) -> BoardSupplier:
        return self.__boardSuplier
    
    def get_board_pane(self):
        return self.__board_pane_holder

    def set_board_pane(self, board_pane_holder):
        self.__board_pane_holder = board_pane_holder

    def get_player(self):
        return self.__player
    
    def __act_turn(self):
        while (len(self.__action_queue) > 0):
            organism = heappop(self.__action_queue)
            if organism.get_symbol() == "P":
                self.__player = organism
            if organism.is_alive():
                organism.act(self)

    def __end_turn(self):
        mapper = self.__organisms.get_mapper()
        keys = list(mapper.keys())
        for key in keys:
            liste = list(filter(lambda x: x.is_alive(), mapper.get(key)))
            for item in liste:
                item.end_turn()
            if len(liste) == 0:
                del mapper[key]
    
    def turn(self):
        print('turn')
        self.__action_queue = []
        for list in self.__organisms.get_all():
            for organism in list:
                if organism.is_alive():
                    heappush(self.__action_queue, organism)
        self.__act_turn()
        self.__end_turn()
        # TODO: redraw
        print('finished')
        self.__board_pane_holder.get().draw()