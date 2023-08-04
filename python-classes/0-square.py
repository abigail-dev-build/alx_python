class Square:
    '''Defining a square by size'''
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def area(self):
        return self.size ** 2

    def perimeter(self):
        return 4 * self.size

