#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent users from instantiating new LockedClass attributes
    except if 'first_name'.
    """
    __slots__ = ["first_name"]
