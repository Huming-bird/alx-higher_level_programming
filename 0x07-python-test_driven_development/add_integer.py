#!/usr/bin/python3
""" 
This is the "add_integer" module
"""

def add_integer(a, b=98):
    """ This function adds two integers.

    Args:

    a : positional argument
    b : keyword argument

    Output:

    The function will return the sum of a and b
    
    >>> add_integer(9)
    107

    """
    
    if not (isinstance(a, (int,float)) and isinstance(b, (int,float))):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
