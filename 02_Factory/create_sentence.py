from sentence import Sentence

def create_standard_sentence():
    sentence = Sentence()
    sentence.add_adjective()
    sentence.add_noun()
    sentence.add_verb()
    sentence.add_adjective()
    sentence.add_noun()
    sentence.show()

def main():

    print("Sentence:")
    create_standard_sentence()

    print("\nAnother one:")
    create_standard_sentence()

    print("\nAnd finally:")
    create_standard_sentence()

if __name__ == "__main__":
    main()
