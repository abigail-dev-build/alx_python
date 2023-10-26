"""
This module is a definition of a class Square that represents a square.


Methods:
    __init__(self, size): Initializes an instance or object of the class
"""
class Square:
    '''Defining the size of  a square'''
    def __init__(self, size=0):
        self.size = size

    '''Getting the size of  a square'''
    def size(self):
        return self.size

    '''Defining property setter to set the size of the square'''
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    '''Defining a square by area'''
    def area(self):
        return self.size ** 2
