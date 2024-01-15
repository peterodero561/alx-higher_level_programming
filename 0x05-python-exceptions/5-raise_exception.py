#!/usr/bin/python3
def raise_exception():
    try:
        result = 2 + '2'
    except TypeError as e:
        print("Exception raised")
