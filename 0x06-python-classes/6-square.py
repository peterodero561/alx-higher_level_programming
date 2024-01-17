#!/usr/bin/python3
'''A class of creating a square object'''


class Square:

    '''Square class
    Fields: size - length of the side of the square
    Methods: area - calculates the area of the square
            size - getter of the side
            size - setter of the side
    '''

    def __init__(self, size=0, position=(0, 0)):

        '''intializes the square'''

        self.size = size
        self.position = position

    @property
    def size(self):

        '''Getter for the length of the square'''

        return self.__size

    @size.setter
    def size(self, value):

        '''
        setter - for setting the size
        '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):

        '''Getter for the position of the square'''

        return self.__position

    @position.setter
    def position(self, value):

        '''
        setter - for setting the position
        '''

        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        '''calculates area of a square'''

        return self.__size ** 2

    def my_print(self):

        '''Prints in the stdout the square with the charcter #'''

        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        else:
            print()
