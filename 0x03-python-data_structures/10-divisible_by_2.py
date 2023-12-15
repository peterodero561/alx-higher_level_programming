#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for i in range(1, len(my_list)):
        if i % 2 == 0:
            list.append("True")
        else:
            list.append("False")
