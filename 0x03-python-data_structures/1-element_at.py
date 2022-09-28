#!/bin/usr/python3
def element_at(my_list, idx):
    if idx < 0:
        response = None
    elif idx > (len(my_list) - 1):
        response = None
    else:
        response = my_list[idx]
    return response
