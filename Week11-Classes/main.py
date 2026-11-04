
# imports the whole file - have to use the module name first
import random

# imports a specific function or class
from random import randint

randint(10,100)

class Chair:

    def __init__(self, minimum_height_in_cm, maximum_height_in_cm, number_of_arms):
        # TODO - come back to this on Wednesday with exceptions
        self._height_in_cm = minimum_height_in_cm
        self._minimum_height_in_cm = minimum_height_in_cm
        self._maximum_height_in_cm = maximum_height_in_cm
        self._number_of_arms = number_of_arms
        self.color = ""

    def change_height(self, change_in_cm):
        self._height_in_cm += change_in_cm
        if self._height_in_cm < self._minimum_height_in_cm:
            self._height_in_cm = self._minimum_height_in_cm
        if self._height_in_cm > self._maximum_height_in_cm:
            self._height_in_cm = self._maximum_height_in_cm

    # UMGPT - Prompt: write the get functions for these attributes
    def get_height_in_cm(self):
        return self._height_in_cm

    def get_minimum_height_in_cm(self):
        return self._minimum_height_in_cm

    def set_minimum_height_in_cm(self, minimum_height_in_cm):
        if minimum_height_in_cm < 0:
            raise ValueError("minimum height can't be less than 0")

        if minimum_height_in_cm > self._maximum_height_in_cm:
            raise ValueError("Can't make minimum greater than maximum")

        if minimum_height_in_cm > self._height_in_cm:
            raise ValueError("Can't max minimum greater than current height")

        self._minimum_height_in_cm = minimum_height_in_cm



    def get_maximum_height_in_cm(self):
        return self._maximum_height_in_cm

    def get_number_of_arms(self):
        return self._number_of_arms

    def __str__(self):
        return f"{self.color} chair currently at {self._height_in_cm} cm"





class Animal:

    # constructors job is to create attributes and give values
    def __init__(self):
        self.name = ""
        self.species = ""
        self.weight_in_grams = 0
        self.height_in_cm = 0

    def __gt__(self, other):
        return other <= self

    def __lt__(self, other):
        return self.weight_in_grams < other.weight_in_grams

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        return self.name == other.name and self.species == other.species \
            and self.weight_in_grams == other.weight_in_grams and self.height_in_cm == other.height_in_cm


def print_animal(animal : Animal):
    print(animal.name)
    print(animal.species)
    print(animal.weight_in_grams)


# only run this, if it's the python file being run
if __name__ == '__main__':

    erics_chair = Chair(10, 50, 2)
    # don't access hidden / private variables
    # erics_chair._height_in_cm = -10
    erics_chair.change_height(10)
    print(erics_chair.get_height_in_cm())
    erics_chair.set_minimum_height_in_cm(100)
    print(erics_chair.get_height_in_cm())
    erics_chair.change_height(10)
    print(erics_chair.get_height_in_cm())
    erics_chair.color = 'Red and grey'
    print(erics_chair)


    olive = Animal()
    olive.name = "Olive"
    olive.species = "Canine"
    olive.height_in_cm = 25
    olive.weight_in_grams = 6000


    print_animal(olive)

    merlin = Animal()
    merlin.name = "Merlin"
    merlin.species = "Feline"
    merlin.height_in_cm = 15
    merlin.weight_in_grams = 5000

    print_animal(merlin)

    print(merlin < olive)

    print(merlin == olive)

    print(olive > merlin)
    print(merlin > olive)

    while True:
        # try something that might raise an exception
        try:
            number = int(input("Enter a number"))
            print(10 / number)
            break
        # bad form to catch generic exception
        # except Exception as error:
        #     print(error)
        except ValueError as error:
            print(error)
        except ZeroDivisionError as error:
            print("you can't divide by 0 try again")






