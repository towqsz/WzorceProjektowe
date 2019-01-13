import abc
import dicts
import random

class AbstractWordFactory(metaclass=abc.ABCMeta):
    """
    Declare an interface for operations that create abstract product
    objects.
    """

    @abc.abstractmethod
    def create_simple_word(self):
        pass

    @abc.abstractmethod
    def create_password(self):
        pass

    @abc.abstractmethod
    def create_noun(self):
        pass

    @abc.abstractmethod
    def create_verb(self):
        pass

    @abc.abstractmethod
    def create_adjective(self):
        pass


class WordFactory1(AbstractWordFactory):
    """
    Implement the operations to create concrete product objects.
    """
    def create_simple_word(self):
        return SimpleWord1()

    def create_password(self):
        return Password1()
    
    def create_noun(self):
        return Noun()

    def create_verb(self):
        return Verb()

    def create_adjective(self):
        return Adjective()


class WordFactory2(AbstractWordFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_simple_word(self):
        return [SimpleWord1()]

    def create_password(self):
        return [Password1()]

    def create_noun(self):
        return [Noun()]

    def create_verb(self):
        return [Verb()]

    def create_adjective(self):
        return [Adjective()]


class AbstractNoun(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class Noun(AbstractNoun):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """
    value = dicts.nouns[random.randint(0, len(dicts.nouns)-1)]
    length = len(value)

    def interface(self):
        pass

class AbstractVerb(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class Verb(AbstractVerb):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """
    value = dicts.verbs[random.randint(0, len(dicts.verbs)-1)]
    length = len(value)
    
    def interface(self):
        pass

class AbstractAdjective(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class Adjective(AbstractAdjective):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """
    value = dicts.adjectives[random.randint(0, len(dicts.adjectives)-1)]
    length = len(value)
    
    def interface(self):
        pass


class AbstractSimpleWord(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class SimpleWord1(AbstractSimpleWord):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface(self):
        pass


class SimpleWord2(AbstractSimpleWord):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface(self):
        pass


class AbstractPassword(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class Password1(AbstractPassword):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface(self):
        pass


class Password2(AbstractPassword):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface(self):
        pass


def main():
    #for factory in (ConcreteFactory1(), ConcreteFactory2()):
    #    product_a = factory.create_product_a()
    #    product_b = factory.create_product_b()
    #    product_a.interface_a()
    #    product_b.interface_b()\
    pass

if __name__ == "__main__":
    main()
