#!/usr/bin/python
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        return (sorted(my_list)[-1])
