#!/usr/bin/python3
'''An empty BaseGeometry class'''


class BaseGeometry:
    '''Empty class'''

    def area(self):
        '''Raises a Exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be an integer".format(name))


class Rectangle(BaseGeometry):
    '''subclass of BaseGeometry'''

    def __init__(self, width, height):
        '''Intializes the sides of a Rectangle object'''
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Calculates the area of a given rectangle object'''
        return self.__width * self.__height

    def __str__(self):
        '''what to print in object'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    '''subclass of Rectangle'''

    def __init__(self, size):
        '''initializes the sides of a square'''
        super().__init__(size, size)
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Calculates the area of a Square'''
        return self.__size ** 2

    def __str__(self):
        '''what to print in object'''
        return "[Square] {}/{}".format(self.__size, self.__size)
