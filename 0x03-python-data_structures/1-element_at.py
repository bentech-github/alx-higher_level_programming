#!/bin/usr/python3
def element_at(my_list, idx):
    if idx < 0:
        response = None
    elif idx > len(my_list):
        response = None
    else:
        response = my_list[idx]
    return response
