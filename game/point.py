from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int
    
    def __getstate__(self) -> object:
        return (self.x, self.y)
    
    def __setstate__(self, state):
        self.__init__(*state)