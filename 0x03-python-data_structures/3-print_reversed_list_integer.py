#!/bin/usr/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for i in range(a):
        print("{:d}".format(my_list[a - 1 - i]))
