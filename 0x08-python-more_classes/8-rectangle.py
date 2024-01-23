#!/usr/bin/python3
'''a rectangle class'''


class Rectangle:
    '''class for a rectangle object'''
    number_of_instances = 0
    print_symblol = "#"

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
        Rectangle.number_of_instances += 1

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
            return ((str(self.print_symbol) * self.width + "\n") *
                    self.height).rstrip()

    def __repr__(self):
        '''
        return a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        '''
        return f"Rectangle(width = {self.width}, height={self.height})"

    def __del__(self):
        '''Says goobye at the deletion of a object'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        return which of a given two rectandle is bigger than the other
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area 2:
            return rect_1
        else:
            return rect_2
