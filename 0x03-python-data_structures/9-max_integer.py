#!/usr/bin/python
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        a = 0
        for value in my_list:
            if value > a:
                a = value 
    return a
