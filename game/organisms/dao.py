from typing import Dict

from game.point import Point


class OrganismDAO:
    from game.organisms.base import OrganismBase
    __mapper: Dict[Point, list[OrganismBase]] = {}
    __counter: Dict[str, int] = {}

    def __insertOrganism(self, organism: OrganismBase):
        position = organism.get_position()
        if position in self.__mapper:
            self.__mapper[position].append(organism)
        else:
            self.__mapper[position] = [organism]

    def spawn(self, organism: OrganismBase):
        name = organism.get_symbol()
        id = 0
        if name in self.__counter:
            id = self.__counter[name]
        self.__counter[name] = id + 1
        organism.set_id(id)
        self.__insertOrganism(organism)

    def get_entity_at(self, position: Point, symbol: str = None) -> OrganismBase|None:
        if position in self.__mapper:
            fill = list(filter(lambda x: x.is_alive() and (symbol == None or x.get_symbol() == symbol), self.__mapper[position]))
            return fill[0] if len(fill) > 0 else None
    
    def move_organism(self, organism: OrganismBase, oldPosition: Point):
        if oldPosition not in self.__mapper:
            return
        list = self.__mapper[oldPosition]
        if len(list) == 1:
            del self.__mapper[oldPosition];
        else:
            self.__mapper[oldPosition].remove(organism)
        self.__insertOrganism(organism)

    def get_mapper(self):
        return self.__mapper
    
    def get_all(self):
        return self.__mapper.values()