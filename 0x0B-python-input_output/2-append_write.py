#!/usr/bin/python3
'''Function that appends a file'''


def append_write(filename="", text=""):
    '''append text to a file'''
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
