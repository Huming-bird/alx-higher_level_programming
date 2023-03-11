#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        maxi = "None"
    else:
        maxi = 0
        for i in range(len(my_list)):
            if my_list[i] > maxi:
                maxi = my_list[i]
    return maxi
