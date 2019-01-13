from factory_method import *

def main():

    print("Noun generator:")
    verb_gen = NounGenerator()
    print("Skorzystaj z interfejsu produktu:")
    verb_gen.product.interface()
    print("Pokaż obiekt:")
    verb_gen.show()

    print("Verb generator:")
    verb_gen = VerbGenerator()
    print("Skorzystaj z interfejsu produktu:")
    verb_gen.product.interface()
    print("Pokaż obiekt:")
    verb_gen.show()

    print("Adjective generator:")
    verb_gen = AdjectiveGenerator()
    print("Skorzystaj z interfejsu produktu:")
    verb_gen.product.interface()
    print("Pokaż obiekt:")
    verb_gen.show()

if __name__ == "__main__":
    main()
