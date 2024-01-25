#!/usr/bin/python3
'''Function that reads a text file'''


def read_file(filename=""):
    '''Reads a text file (UTF8) and prints if to stdout'''
    with open(filename, encoding="utf-8") as f:
        print(f.read())
