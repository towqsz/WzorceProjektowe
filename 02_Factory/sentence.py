from factory_method import *

class Sentence:

    def __init__(self):
        self.sentence = []
        self.noun_gen = NounGenerator()
        self.verb_gen = VerbGenerator()
        self.adjective_gen = AdjectiveGenerator()
    
    def add_verb(self):
        self.verb_gen.gen_new_word()
        self.sentence.append(self.verb_gen.product.value)

    def add_noun(self):
        self.noun_gen.gen_new_word()
        self.sentence.append(self.noun_gen.product.value)

    def add_adjective(self):
        self.adjective_gen.gen_new_word()
        self.sentence.append(self.adjective_gen.product.value)

    def show(self):
        sentence_str = " ".join(self.sentence) + "."
        sentence_str = sentence_str.lower()
        
        print(sentence_str)

