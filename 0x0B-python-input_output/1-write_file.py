#!/usr/bin/python3
'''Function that writes a string to a file'''


def write_file(filename="", text=""):
    '''writes a string to a file and returns the number of character'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
