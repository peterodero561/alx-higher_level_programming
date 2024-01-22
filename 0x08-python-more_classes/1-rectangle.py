#!/usr/bin/python3
'''a rectangle class'''


class Rectangle:
    '''class for a rectangle object'''

    @property
    def height(self):
        '''getter for the height of the rectangle object'''

        self._height = height

    @height.setter
    def height(self, value):
        '''Setter for the height of the rectangle object'''

        if not isinstance(value, int):
            raise TypeError('height Must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self._height = value


    @property
    def width(self):
        '''getter for the width of the rectangle object'''

        self._width = width

    @width.setter
    def width(self, value):
        '''Setter for the width of the rectangle object'''

        if not isinstance(value, int):
            raise TypeError('width Must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self._width = value

    def __init__(self, width=0, height=0):
        '''init - initializes the height and the width'''

        self.width = width
        self.height = height
        self._width = 0
        self._height = 0

