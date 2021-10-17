# Course: CS261 - Data Structures
# Student Name: Edgar Palaquibay
# Assignment: 2
# Description: This script contains a stack implementation utilizing the Dynamic array file imported.
# The newly implemented methods are push(), pop(), top()

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Input: value (object)
        Output: None
        This function pushes a value onto the current stack,
        """
        self.da_val.append(value)

    def pop(self) -> object:
        """
        Input: N/A
        Output: object
        This function will remove the top element from the stack and will return the value. If the stack
        is empty then it will raise a custom "StackException"

        """
        if self.is_empty():
            raise StackException()
        else:
            value = self.da_val.get_at_index(self.size() - 1) #capture value before it is removed
            self.da_val.remove_at_index(self.size() - 1)
            return value

    def top(self) -> object:
        """
        Input: N/A
        Output: Object
        This function will return the top element in the stack, but will not delete it. If the stack is empty
        it will raise a StackException() error.
        """
        if self.is_empty():
            raise StackException()
        return self.da_val.get_at_index(self.size() - 1)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
