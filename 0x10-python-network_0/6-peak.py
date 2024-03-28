#!/usr/bin/python3
'''Module for find_peak_function'''


def find_peak(list_of_integers):
    '''Finds peak(No greater than its neighbours) in a given list'''
    size = len(list_of_integers)
    for i in range(1, size-1, 1):
        if (list_of_integers[i] >= list_of_integers[i+1] and
                list_of_integers[i] >= list_of_integers[i-1]):
            return list_of_integers[i]
        else:
            continue
