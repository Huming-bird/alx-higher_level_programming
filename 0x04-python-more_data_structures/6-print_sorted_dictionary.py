#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    holder = sorted(a_dictionary.keys())
    new = {}

    for keys in holder:
        new[keys] = a_dictionary[keys]
    for key, value in new:
        print(f"{key}: {value}")
