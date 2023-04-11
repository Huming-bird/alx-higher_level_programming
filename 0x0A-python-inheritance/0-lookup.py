#!/usr/bin/python3
""" returns a list of available attributes and methods of an object """


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
