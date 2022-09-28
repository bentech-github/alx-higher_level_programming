#!/usr/bin/python3
def no_c(my_string):
    answer = ""
    for char in my_string:
        if char.lower() != 'c':
            answer += char
    return answer
