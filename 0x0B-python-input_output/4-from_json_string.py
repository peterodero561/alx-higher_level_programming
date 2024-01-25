#!/usr/bin/python3
'''function that returns the JSON representation of an object (string)'''


import json


def from_json_string(my_obj):
    '''returns the object represented by JSON string'''
    return json.loads(my_obj)
