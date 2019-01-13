import random
import dicts


class WordFactory(object):
    def element(self, type):
        if type == "SimpleWord": return SimpleWord()
        elif type == "Password": return Password()
        elif type == "Noun": return Noun()
        elif type == "Verb": return Verb()
        elif type == "Adjective": return Adjective()
        assert 0, "Bad word creation: " + type


class SimpleWord(WordFactory):
    value = "Word"
    length = len(value)

class Password(WordFactory):
    value = "Password1234"
    length = len(value)


class Noun(WordFactory):
    value = dicts.nouns[random.randint(0, len(dicts.nouns)-1)]
    length = len(value)

class Verb(WordFactory):
    value = dicts.verbs[random.randint(0, len(dicts.verbs)-1)]
    length = len(value)

class Adjective(WordFactory):
    value = dicts.adjectives[random.randint(0, len(dicts.adjectives)-1)]
    length = len(value)
