#!/usr/bin/python3

def no_c(my_string):
    for xter in my_string:
        if xter in "Cc":
            continue
        print("{}".format(xter), end='')
    print('')
