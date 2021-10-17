# Course: CS261 - Data Structures
# Student Name: Edgar Palaquibay
# Assignment: 2
# Description: This script is a max stack implementation using dynamic arrays. The newly implemented
# methods are push(), pop(), top(), get_max().

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
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
        Output: N/A
        This function will add a new element to the stop of the stack
        """
        if self.size() == 0:
            self.da_val.append(value)
        if self.da_max.length() == 0:
            self.da_max.append(value)

        elif value <= self.da_max.get_at_index(self.da_max.length()-1):
            arg = self.da_max.get_at_index(self.da_max.length()-1)
            self.da_max.append(arg) #append the current max of da_max onto da_max again
            self.da_val.append(value)
        else:
            self.da_max.append(value) #append the value argument to da_max since it's larger than current max
            self.da_val.append(value)

    def pop(self) -> object:
        """
        Input: N/A
        Output: object
        This function returns the top value of the da_val stack, it also removes the top value from da_max stack but
        does not return it
        """
        if self.is_empty():
            raise StackException()
        else:
            value = self.da_val.get_at_index(self.size() - 1)  #capture the top value of the stack before removing
            self.da_val.remove_at_index(self.size() - 1)
            self.da_max.remove_at_index(self.da_max.length() - 1)
            return value

    def top(self) -> object:
        """
        Input: N/A
        Output: object
        This function will return the top value of the da_val stack and raise an exception if empty
        """
        if self.is_empty():
            raise StackException()
        return self.da_val.get_at_index(self.da_val.length() - 1) #return top of stack

    def get_max(self) -> object:
        """
        Input: N/A
        Output: object
        This function returns the maximum value that is in the stack, if the stack is empty the method raises a
        "StackException"
        """
        if self.is_empty():
            raise StackException()
        return self.da_max.data[self.da_max.length() - 1] #return top of max stack






# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = MaxStack()
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
    s = MaxStack()
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


    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
