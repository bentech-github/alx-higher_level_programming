#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    good = []
    for i in my_list:
        if i % 2 == 0:
            good.append(True)
        else:
            good.append(False)
    return good
