#!/usr/bin/python3

def roman_to_int(roman_string):
    dic = { 
        'I': 1
        'V': 5
        'X': 10
        'L': 50
        'C': 100
        'D': 500
        'M': 1000
    }
    if type(roman_string) != str or roman_string == None:
        answer = 0
    else:
