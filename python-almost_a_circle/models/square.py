"""
Square Module

This module defines a square

Classes:
- Base - Represents base class for rest of classes
- Rectangle: Represents a rectangle inherited from Base class
- Square: Represents a square inherited from Rectangle
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
        Representing a square

        Parameters:
        size (int): size of the square
        x (int): x position of square
        y (int): y position of square
        id : Identifier of square
        """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes rectangle instance with  size, x, y and id.

        Parameters:
        Parameters:
        size (int): size of the square
        x (int): x position of square
        y (int): y position of square
        id : Identifier of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """
        Give access to size attr
        """
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value