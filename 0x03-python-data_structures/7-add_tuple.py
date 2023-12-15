#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = (tuple_a + (0, 0))[:2]  # Ensure at least two elements
    b = (tuple_b + (0, 0))[:2]  # Ensure at least two elements
    new_tup = (a[0] + b[0], a[1] + b[1])
    return new_tup
