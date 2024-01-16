#!/usr/bin/python3
class Square:
    '''An empty class tha defines a square'''
    def __init__(self, side):
        '''initializes the side of the square'''
        self.side = side
    def area(self):
        '''claculates the area of a given square
        Returns: area of a square
        '''
        return side * side
    def perimeter(self):
        '''claculates the perimeter of a given square
        Returns: perimeter of a square
        '''
        return side * 4
