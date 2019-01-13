from simple_factory import *

def main():

    factory = WordFactory()
    print("Stworz Noun:")
    noun = factory.element("Noun")
    print(noun)
    print(noun.value)
    print(noun.length)

    print("\nStworz Verb:")
    verb = factory.element("Verb")
    print(verb)
    print(verb.value)
    print(verb.length)

    print("\nStworz Adjective:")
    adjective = factory.element("Adjective")
    print(adjective)
    print(adjective.value)
    print(adjective.length)

if __name__ == "__main__":
    main()
