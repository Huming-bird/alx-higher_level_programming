#!/usr/bin/python3
def islower(c):
    if type(c) == str:
        return c.islower()
    elif type(c) == int:
        return chr(c).islower()
