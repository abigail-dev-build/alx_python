"""
Rectangle Module

This module defines a rectangle

Classes:
- Base - Represents base class for rest of classes
- Rectangle: Represents a rectangle inherited from Base class
"""

from models.base import Base

class Rectangle(Base):
    """
    Representsg a rectangle

    Attributes:
    width (int): width of the rectangle
    height (int): height of the rectangle
    x (int): x position o rectangle
    y (int): y position of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes rectangle instance with  widht, height, x and y.

        Parameters:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x position of rectangle
        y (int): y position of rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.validate_width()
        self.validate_height()
        self.validate_x()
        self.validate_y()

    def validate_width(self):
        """
        validates the arguments passed into the object
        """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")
        
    def validate_height(self):
        """
        validates the arguments passed into the object
        """  
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")
       
    def validate_x(self):
        """
        validates the arguments passed into the object
        """
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")
        
    def validate_y(self):
        """
        validates the arguments passed into the object
        """
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """
        Gives access to the private attribute

        Returns:
        int: the private attribute of width
        """
        return self.__width
    
    @width.setter
    def width(self, width):
        """
        Sets value and validation for private attribute

        attribute:
        width: the width of rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Gives access to the private attribute

        Returns:
        int: the private attribute of height
        """
        return self.__height
    
    @height.setter
    def height(self, height):
        """
        Sets value and validation for private attribute

        attribute:
        height: the height of rectangle
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Gives access to the private attribute

        Returns:
        int: the private attribute of x
        """
        return self.__x
    
    @x.setter
    def x(self, x):
        """
        Sets value and validation for private attribute

        attribute:
        x: the x position of rectangle
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Gives access to the private attribute

        Returns:
        int: the private attribute of y
        """
        return self.__y
    
    @y.setter
    def y(self, y):
        """
        Sets value and validation for private attribute

        attribute:
        y: the y position of rectangle
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0".format(y))
        self.__y = y

    def area(self):
        """
        Computes area of the Rectangle

        Returns:
        area value of the Rectangle
        """
        return self.__width * self.__height
    
    def display(self):
        """
        prints in stdout the Rectangle 
        instance with the character #
        """
        for space in range(0, self.__y):
                print()
        for i in range(0, self.__height):
            for tab in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """
        by overriding the __str__ of Rectangle
        Return:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        for key, value in kwargs.items():
            if args is True:
                break
            if key == 'width':
                self.__width = value
            elif key == 'height':
                self.__height = value
            elif key == 'x':
                self.__x = value
            elif key == 'y':
                self.__y = value
            elif key == 'id':
                self.id = value

        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]