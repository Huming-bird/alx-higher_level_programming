#!/usr/bin/python3

def best_score(a_dictionary):
    if len(a_dictionary) < 1:
        best = 'None'
    else:
        best = 0
        for key in a_dictionary:
            if a_dictionary[key] > best:
                best = a_dictionary[key]
    for keys, value in a_dictionary.items():
        if best == value:
            break
    return keys
