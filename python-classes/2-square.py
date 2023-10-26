"""
This module is a definition of a class Square that represents a square.


Methods:
    __init__(self, size): Initializes an instance or object of the class

    area: Returns the area of the square
"""
class Square():
    '''Defining the size of  a square
        Methods:
        __init__(self, size): Initializes a Square object with the given size.
        area: Returns the area of the square
    '''
    def __init__(self, size=0):
        """Initialize a square instance
            Args:
                size(int): the size of the square initialized to 0
                """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size  < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Defining method for area of a square'''
        return self.__size ** 2
