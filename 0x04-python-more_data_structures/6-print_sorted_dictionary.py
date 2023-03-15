#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    holder = sorted(a_dictionary.keys())

    for keys in holder:
        print('{}: {}'.format(keys, a_dictionary.get(keys)))
