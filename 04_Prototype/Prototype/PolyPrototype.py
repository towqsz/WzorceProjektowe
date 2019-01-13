from abc import ABC, abstractmethod
import copy

class PolyPrototype(ABC):
    @abstractmethod
    def Clone():
        pass

class Poly(PolyPrototype):
    _sides = None
    _length = None

    def __init__(self, sides, length):
        self._sides = sides
        self._length = length

    def Clone(self):
        print("Cloning...")
        return copy.copy(self)

    @property
    def sides(self):
        return self._sides

    @property
    def length(self):
        return self._length

    @sides.setter
    def sides(self, sides):
        self._sides = sides

    @length.setter
    def length(self, length):
        self._length = length

    def show(self):
        print("Sides: {}".format(self._sides))
        print("Side length: {}".format(self._length))
