#!/usr/bin/python3

""" This module contains a function that returns the json
format of an object """

import json


def to_json_string(my_obj):
    """ This fnc returns the json format of my_obj """
    return json.dumps(my_obj)
