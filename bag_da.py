# Course: CS261 - Data Structures
# Student Name: Edgar Palaquibay
# Assignment: 2
# Description: This script is a bag implementation, besides given methods the implemented ones are
# add(), remove(), count(), clear(), equal()

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Input: value (object)
        Output: None
        This method add a new element to the bag
        """
        self.da.append(value)


    def remove(self, value: object) -> bool:
        """
        Input: value(object)
        Output: bool
        This method removes any one element from the bag that matches the provided value argument
        object. The method returns True if some object was actually removed from the bag.
        Otherwise, it returns False.
        """
        for el in range(self.da.length()):
            if self.da.get_at_index(el) == value:
                self.da.remove_at_index(el)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Input: value(object)
        Output: int
        This method count will count the number of elements in the
        bag that match the provided value.
        """
        counter = 0
        for el in range(self.da.length()):
            if self.da.get_at_index(el) == value:
                counter += 1
        return counter

    def clear(self) -> None:
        """
        Input: N/A
        Output: None
        This function clears the current dynamic array but setting it to an empty dynamic array
        """
        self.da=DynamicArray()


    def equal(self, second_bag: object) -> bool:
        """
        Input: second_bag (object)
        Output: bool
        This function will return a bool value of true or false. True if the two bags
        have the same number of elements and same elements, order does not matter. False otherwise.
        """
        if self.da.length() != second_bag.da.length():
            return False

        for el in range(self.da.length()):
            element = self.da.get_at_index(el)
            if (self.count(element) != second_bag.count(element)):
                return False
        return True


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
