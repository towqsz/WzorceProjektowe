"""
Define an interface for creating an object, but let subclasses decide
which class to instantiate. Factory Method lets a class defer
instantiation to subclasses.
"""

import abc
import dicts
import random


class AbstractWordGenerator(metaclass=abc.ABCMeta):
    """
    Declare the factory method, which returns an object of type Product.
    WordGenerator may also define a default implementation of the factory
    method that returns a default ConcreteProduct object.
    Call the factory method to create a Product object.
    """
    word_list = []
    def __init__(self):
        self.product = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass

    def show(self):
        print("\nWygenerowane slowo to: {}".format(self.product.value))
        print("Jego dlugosc to: {}".format(self.product.length))
        print("_"*50)

    def gen_new_word(self):
        self.product.value = self.product.word_dict[random.randint(0, len(self.product.word_dict)-1)]
        self.product.length = len(self.product.value)


class NounGenerator(AbstractWordGenerator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct1.
    """

    def _factory_method(self):
        return Noun()


class VerbGenerator(AbstractWordGenerator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct2.
    """

    def _factory_method(self):
        return Verb()

class AdjectiveGenerator(AbstractWordGenerator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct2.
    """

    def _factory_method(self):
        return Adjective()


class AbstractWord(metaclass=abc.ABCMeta):
    """
    Define the interface of objects the factory method creates.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class SimpleWord(AbstractWord):
    """
    Implement the Product interface.
    """

    def interface(self):
        pass


class Password(AbstractWord):
    """
    Implement the Product interface.
    """

    def interface(self):
        pass

class Noun(AbstractWord):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """
    word_dict = dicts.nouns
    value = dicts.nouns[random.randint(0, len(dicts.nouns)-1)]
    length = len(value)

    def interface(self):
        print(self.value)
        print(self.length)



class Verb(AbstractWord):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """
    word_dict = dicts.verbs
    value = dicts.verbs[random.randint(0, len(dicts.verbs)-1)]
    length = len(value)
    
    def interface(self):
        print(self.value)
        print(self.length)


class Adjective(AbstractWord):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """
    word_dict = dicts.adjectives
    value = dicts.adjectives[random.randint(0, len(dicts.adjectives)-1)]
    length = len(value)
    
    def interface(self):
        print(self.value)
        print(self.length)


