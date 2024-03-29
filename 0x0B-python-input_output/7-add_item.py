#!/usr/bin/python3

""" This module contains fnc that adds all args to a list """

import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    
    try:
        my_obj = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_obj = []
        my_obj.extend(sys.argv[1:])
        save_to_json_file(my_obj, 'add_item.json')
