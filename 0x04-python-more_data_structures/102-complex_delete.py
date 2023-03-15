#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = a_dictionary.keys()

    for key in key_list:
        while key in a_dictionary:
            del(a_dictionary[key])
    return a_dictionary
