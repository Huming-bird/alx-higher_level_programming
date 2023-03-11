#!/usr/bin/python3

def no_c(my_string):
    for xter in my_string:
        if xter == 'c'.islower() or xter == 'c'.isupper():
            pass
        print("{}".format(xter), end='')
    print('')
