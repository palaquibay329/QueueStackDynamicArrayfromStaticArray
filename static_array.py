# Course: CS261 - Data Structures
# Description: Static Array class


class StaticArrayException(Exception):
    """
    Custom exception for Static Array class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class StaticArray:
    """
    Class that implements Static Array Data Structure
    Implemented methods: init, get, set, size


    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self, size=10):
        """
        Create array of given size
        Initialize all elements with values of None
        If requested size is not a positive number, raise StaticArray Exception
        """
        if size < 1:
            raise StaticArrayException
        self._data = [None] * size

    def __str__(self):
        """
        Return content of static array in human-readable form
        """
        out = "STAT_ARR Size: "
        out += str(len(self._data))
        out += " " + str(self._data)
        return out

    def get(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises StaticArrayException
        """
        if index < 0 or index >= self.size():
            raise StaticArrayException
        return self._data[index]

    def set(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises StaticArrayException
        """
        if index < 0 or index >= self.size():
            raise StaticArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get() method above, but called differently
        These snippets of code are equivalent:

        arr = StaticArray()
        arr.set(0, 'hello')
        print(arr.get(0))

        arr = StaticArray()
        arr[0] = 'hello'
        print(arr[0])
        """
        return self.get(index)

    def __setitem__(self, index, value) -> object:
        """
        Same functionality as set() method above, but called differently
        These snippets of code are equivalent:

        arr = StaticArray()
        arr.set(0, 'hello')
        print(arr.get(0))

        arr = StaticArray()
        arr[0] = 'hello'
        print(arr[0])
        """
        self.set(index, value)

    def size(self):
        """ Return size of the array (number of elements) """
        return len(self._data)
