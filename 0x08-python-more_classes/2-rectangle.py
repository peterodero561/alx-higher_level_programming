#!/usr/bin/python3
'''a rectangle class'''


class Rectangle:
    '''class for a rectangle object'''

    @property
    def height(self):
        '''getter for the height of the rectangle object'''

        self.__height = height

    @height.setter
    def height(self, value):
        '''Setter for the height of the rectangle object'''

        if not isinstance(value, int):
            raise TypeError('Width Must be an integer')
        elif value < 0:
            raise ValueError('Width must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        '''getter for the width of the rectangle object'''

        self.__width = width

    @width.setter
    def width(self, value):
        '''Setter for the width of the rectangle object'''

        if not isinstance(value, int):
            raise TypeError('Width Must be an integer')
        elif value < 0:
            raise ValueError('Width must be >= 0')
        else:
            self.__width = value

    def __init__(self, width=0, height=0):
        '''init - initializes the height and the width'''

        self.width = width
        self.height = height

    def area(self):
        '''Calculates the area of the rectangle object'''

        return self.__width * self.__height

    def perimeter(self):
        '''Calculates the perimeter of the rectangle object'''

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
