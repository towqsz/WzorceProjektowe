from PolyManager import PolyManager
from PolyPrototype import Poly, colorType


def main():
    manager = PolyManager()
    manager.set_poly(1, Poly(60, 20, colorType.RED))
    manager.set_poly(2, Poly(30, 40, colorType.GREEN))
    manager.set_poly(3, Poly(90, 70, colorType.BLUE))

    manager.set_poly(4, manager.get_poly(1))
    manager.get_poly(4).sides_num=4
    
    print("Are objects 1 and 4 the same object?")
    print(manager.get_poly(1) is manager.get_poly(4))
    manager.get_poly(1).show()
    manager.get_poly(4).show()

    print("\nIs shallow copy enough?")
    manager.set_poly(6, manager.get_poly(1).shallow_copy())
    print("Poly 1:")
    manager.get_poly(1).show()
    print("Change something in poly 6.")
    manager.get_poly(6).set_side(20, colorType.GREEN)
    print("Poly 1 and 6")
    manager.get_poly(1).show()
    manager.get_poly(6).show()
    

    print("")
    manager.set_poly(5, manager.get_poly(1).Clone())
    print("Are objects 1 and 5 the same object?")
    print(manager.get_poly(1) is manager.get_poly(5))

    print("\nChange something.")
    manager.get_poly(5).sides_num=8
    
    manager.get_poly(1).show()
    manager.get_poly(5).show()


if __name__ == '__main__':
    main()

