#!/usr/bin/python3


'''
A class of a square
'''


class Square:

    '''
    class defining a square
    Atrributes:
    size - private object variable of the sqaure size
    Methods:
    __init__() - initializes the side of the square
    '''
    def __init__(self, size=0):
        '''
        initializes a square's side
        Parameters:
        size - side of the square
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >0")
        else:
            self.__size = size
