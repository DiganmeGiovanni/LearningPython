""" Models entities """
import random
from entities.exceptions import DrinkException


class Person(object):
    """ Person entity """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def take_drink(self):
        if self.age < 18:
            raise DrinkException('Only adults can take a drink')
        else:
            print('%{} is taking a drink', self.name)

    @staticmethod
    def random_age():
        print('Random age:', random.randint(0, 100))

    @staticmethod
    def random_decimal():
        print('Random decimal:', random.random())

    def __add__(self, other):
        return self.age + other.age

    def __le__(self, other):
        return self.age <= other.age

    def __lt__(self, other):
        return self.age < other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __gt__(self, other):
        return 'String value'


class SoftwareEngineer(Person):
    """ Software engineer person """

    def __init__(self, name, age, main_language):
        super().__init__(name, age)
        self.main_language = main_language

    def write_code(self):
        print('Coding in', self.main_language)
