#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        No = 0
        for i in my_list:
            if i > No:
                No = i
        return No
