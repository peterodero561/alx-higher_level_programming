#!/usr/bin/python3
'''Class student'''


class Student:
    '''student class'''

    def __init__(self, first_name, last_name, age):
        '''initializes object of Student class'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrives a dictionary representation of Student instance'''
        jsonDict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                jsonDict[key] = value
        return jsonDict
