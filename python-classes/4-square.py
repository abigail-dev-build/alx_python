"""
This module is a definition of a class Square that represents a square.


Methods:
    __init__(self, size): Initializes an instance or object of the class
"""
class Square():
    '''Defining the size of  a square
    A class that represents a square
    
    Attributes:
        size(int): The size of the square

    Methods:
        __init__(self, size): Initializes a Square object with the given size.
        area: Returns the area of the square
        @property: A getter to retrieve private instance attribute
        @size.setter: A setter that sets the value to the priv. att

    '''
    def __init__(self, size=0):
        """Initialize a square instance
            Args:
                size(int): the size of the square initialized to 0
                """
        self.__size = size
        
    @property
    def size(self):
        """A getter to retrieve private instance attribute
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        A setter that sets the value to the priv. att

        Args:
        value: the size of the square
        """
        if value != int(value):
            raise TypeError("size must be an integer")
        if value  < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Defining method for area of a square'''
        return self.__size ** 2

    def my_print(self):
        """
        Public method that prints square of #
        """
        if self.__size == 0:
            print()
        # else:
            # for _ in range(self.__size):
            #     print("#" * self.size)
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
            