#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        l = 0
        c = None
        return l , c
    else:
        l = length
        c = sentence[0]
        return l, c
