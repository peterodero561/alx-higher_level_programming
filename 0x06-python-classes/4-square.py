#!/usr/bin/python3
'''A class of creating a square object'''
class Square:
    '''Square class
    Fields: size - length of the side of the square
    Methods: area - calculates the area of the square
            size - getter of the side
            size - setter of the side
    '''
    def __init__(self, size=0):
        '''intializes the square'''
        self.size = size

    @property
    def size(self):
        '''Getter for the length of the square'''
        return self.size
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
    def area(self):
        '''calculates area of a square'''
        return self.__size ** 2
