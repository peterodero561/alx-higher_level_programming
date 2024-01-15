#!/usr/bin/python3
def raise_exception():
    try:
        result = 2 + '2'
    except TypeError as te:
        print("Exception raised")
