# Course: CS261 - Data Structures
# Student Name: Edgar Palaquibay
# Assignment: 2
# Description: This script is a queue implementation using dynamic arrays. The newly implemented methods
# are enqueue() and dequeue()

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da[i]) for i in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        input: value (obj)
        output: N/A
        This function will add a new value to the end of the queue
        """
        self.da.append(value)

    def dequeue(self) -> object:
        """
        Input: N/A
        Output: object
        This method removes and returns the value at the beginning of the queue, if the queue is empty then
        QueueException() iS raised.
        """
        if self.is_empty():
            raise QueueException()

        if self.da.data[0] is not None:
            returnval = self.da[0] #capture the value in the beggining of queue before removing
            self.da.remove_at_index(0)
            return returnval


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
