#!/usr/bin/python3
"""Module defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints a sorted list in ascending order."""
        print(sorted(self))
