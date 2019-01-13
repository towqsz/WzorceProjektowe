from abc import ABC, abstractmethod
import copy

class colorType():
    RED = {"Red": hex(0xFF), "Green": 0, "Blue": 0}
    GREEN = {"Red": 0, "Green": hex(0xFF), "Blue": 0}
    BLUE = {"Red": 0, "Green": 0, "Blue": hex(0xFF)}

class PolyPrototype(ABC):
    @abstractmethod
    def Clone():
        pass

class Color():
    _color = {"Red": None, "Green": None, "Blue": None}

    def __init__(self, color: colorType):
        self._color = color

    def show(self):
        print(self._color)

    def get_color(self):
        return self._color

    some_list = []

class Side():
    _length = None
    _color = None

    def __init__(self, color, length):
        self._length = length
        self._color = Color(color)

    def show(self):
        print("Length: {}".format(self._length))
        self._color.show()
        
class Poly(PolyPrototype):
    _sides_num = None
    _side = None

    def __init__(self, sides, length, color):
        self._sides_num = sides
        self._side = Side(color, length)

    def Clone(self):
        print("Cloning.")
        return copy.deepcopy(self)

    def shallow_copy(self):
        print("Cloning.")
        return copy.copy(self)

    @property
    def sides_num(self):
        return self._sides_num

    @property
    def side(self):
        return self._side

    @sides_num.setter
    def sides_num(self, sides):
        self._sides_num = sides

    def set_side(self, length, color):
        self._side._length = length
        self._side._color._color = color

    def show(self):
        print("Sides: {}".format(self._sides_num))
        self._side.show()
