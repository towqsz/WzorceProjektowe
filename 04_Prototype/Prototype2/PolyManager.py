from PolyPrototype import Poly, PolyPrototype


class PolyManager:
    def __init__(self):
        self._poly_database = {}

    def get_poly(self, name)->PolyPrototype:
        return self._poly_database[name]

    def set_poly(self, name, poly: PolyPrototype):
        self._poly_database.update({name: poly})
