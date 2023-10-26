"""
This Class is the base for subsequent projects
"""

class Base:
    """
    Base class for subsequent tasks
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Class constructor. Pass attributes to objects
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects