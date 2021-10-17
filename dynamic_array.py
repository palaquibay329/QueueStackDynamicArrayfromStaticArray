    # Course: CS261 - Data Structures
# Student Name: Edgar Palaquibay
# Assignment: 2
# Description: This script contains dynamic array class made from a static array, certain methods have been implemented.
# The implemented methods added to the existing skeleton code are resize(), append(), insert_at_index(),
# remove_at_index(), slice(), merge(), map(), filter(), reduce()

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Input: new_capacity (int)
        Output: N/A

        This function will intake a new capacity and will create a new array with that capacity and copy all the values
        from the current array. It also performs checks beforehand, the new capacity must be less than the current size
        of the current array and must be a positive integer.
        """

        if new_capacity < self.size or new_capacity < 1:
            pass
        else:
            self.capacity = new_capacity
            newArr = StaticArray(new_capacity)
            for el in range(self.size):
                newArr[el] = self.data[el]
            self.data = newArr


    def append(self, value: object) -> None:
        """
        Input: value (object)
        Output: N/A

        This function appends a value at the end of an array, but first it checks if it's full, if so then it will
        double in capacity and finally perform the appending.
        """

        if self.size == self.capacity:
            self.resize(2 * self.capacity)


        for el in range(self.capacity):
            if self.data[el] is None:
                self.data[el] = value
                self.size += 1
                break

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Input: index (int), value (object)
        Output: N/A
        This function will insert the given value object into the given index. First it checks if the given index is
        valid, then checks if it needs to double the capacity of the array, and shifts all the elements starting
        from the given index forward by 1, then inserts the value in the specified index. Size increases by 1 as well.

        """
        if index < 0 or index>self.size:
            raise DynamicArrayException

        if self.size == self.capacity:
            self.resize(2 * self.capacity)

        for el in range(self.size, index, -1):
            self.data[el]=self.data[el-1]

        self.data[index]= value
        self.size += 1


    def remove_at_index(self, index: int) -> None:
        """
        Input: index (int)
        Output: N/A
        This function intakes an index and will search for that index in the array and remove it.
        It also changes capacity to twice the size or capacity to 10.

        """
        if index < 0 or index > self.size -1:
            raise DynamicArrayException

        if self.size < (.25 * self.capacity) and self.size * 2 >= 10:
            self.resize(2 * self.size)
        elif self.size < (self.capacity / 4) and self.size * 2 < 10 and self.size >1 :
            self.resize(10)

        for el in range(index, self.size - 1, 1):
            self.data[el] = self.data[el+1]
        self.data[self.size - 1] = None
        self.size -= 1

    def slice(self, start_index: int, size: int) -> object:
        """
        Input: start_index(int), size(int)
        Output: object
        This function will return a dynamic array object based on the start index, will perform checks
        to see if the inputs are valid.
        """
        if start_index < 0 or start_index > self.size -1 or size < 0:
            raise DynamicArrayException
        if (start_index + size -1) > self.size-1:
            raise DynamicArrayException

        final_index= start_index + size
        Dynarr_input= [self.data[i] for i in range (start_index, final_index, 1)]
        return DynamicArray(Dynarr_input)

    def merge(self, second_da: object) -> None:
        """
        Input: second_da (object)
        Output: N/A

        This function will intake a dynamic array and appends it at the end of the current one.
        It calls the append function which takes care of adjusting the capacity.
        """
        for el in range(second_da.size):
            self.append(second_da.data[el])

    def map(self, map_func) -> object:
        """
        Input: map_func is a function that takes a value and returns another based on the function
        Output: object
        In this function a new dynamic array is return, based on the current array and the map_func
        that was passed.
        """
        ret_arr = [self.data[i] for i in range(self.capacity)]
        final_arr = DynamicArray(ret_arr)
        final_arr.size = self.size
        final_arr.capacity = self.capacity
        for el in range(final_arr.size):
            final_arr.data[el] = map_func(final_arr.data[el])
        return final_arr


    def filter(self, filter_func) -> object:
        """
        Input: filter_func (obj)
        Output: object
        This function will pass all the values into filter_func with a for loop, then if the function returns
        True it will append the element that was passed onto filter_func into a newly created dynamic array
        """
        ret_arr = DynamicArray()
        for el in range(self.size):
            if filter_func(self.data[el]):
                ret_arr.append(self.data[el])
        return ret_arr


    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Input: reduce_func (obj), initializer (optional)
        Output: object
        This function will apply reduce_func to all elements of the Dynamic array and will result in a return value
        If a parameter was not provided the first value in the array is used as the initializer.
        """
        if self.is_empty(): #if dynamic array is empty the method returns the value of the initializer
            return initializer

        if initializer is None:
            final_sum = self.data[0]
            for el in range(1,self.size):
                final_sum = reduce_func(final_sum,self.data[el])
        elif initializer is not None:
            final_sum = initializer
            for el in range(0, self.size):
                if self.data[el] is not None:
                    final_sum = reduce_func(final_sum, self.data[el])

        return final_sum

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5,10,15,20,25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
