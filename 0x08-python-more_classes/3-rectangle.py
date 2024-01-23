#!/usr/bin/python3
'''a rectangle class'''


class Rectangle:
    '''class for a rectangle object'''

    @property
    def height(self):
        '''getter for the height of the rectangle object'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for the height of the rectangle object'''

        if not isinstance(value, int):
            raise TypeError('height Must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        '''getter for the width of the rectangle object'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for the width of the rectangle object'''

        if not isinstance(value, int):
            raise TypeError('width Must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def __init__(self, width=0, height=0):
        '''init - initializes the height and the width'''

        self.width = width
        self.height = height

    def area(self):
        '''Calculates the area of the rectangle object'''

        return self.width * self.height

    def perimeter(self):
        '''Calculates the perimeter of the rectangle object'''

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        '''prints the rectangle with the character #
            if either width or height is 0 an empty string is attached
        '''
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width] * self.height)
