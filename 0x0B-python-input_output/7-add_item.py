#!/usr/bin/python3

""" This module contains fnc that adds all args to a list """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_obj = load_from_json_file(filename)
save_to_json_file(my_obj, add_item.json)
