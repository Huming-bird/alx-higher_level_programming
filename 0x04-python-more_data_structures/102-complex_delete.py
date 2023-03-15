#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = a_dictionary.items()

    for items in key_list:
        if items[-1] == value:
            del(a_dictionary[items[0]])
    return a_dictionary
