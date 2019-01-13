from abstract_factory import *

def main():

    factory = WordFactory1()
    print("Stworz Noun:")
    noun = factory.create_noun()
    print(noun)
    print(noun.value)
    print(noun.length)

    print("\nStworz Verb:")
    verb = factory.create_verb()
    print(verb)
    print(verb.value)
    print(verb.length)

    print("\nStworz Adjective:")
    adjective = factory.create_adjective()
    print(adjective)
    print(adjective.value)
    print(adjective.length)

if __name__ == "__main__":
    main()
