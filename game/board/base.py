from abc import ABC, abstractmethod

from game.point import Point

class BoardSupplier(ABC):
    @abstractmethod
    def get_new_position(self, current: Point, move: int) -> Point:
        pass

    @abstractmethod
    def neighbours(self) -> int:
        pass

    @abstractmethod
    def is_legal_position(self, position: Point) -> bool:
        pass