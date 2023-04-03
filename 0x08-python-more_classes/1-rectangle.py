#!/usr/bin/python3
""" This module is about a rectangle class """

class Rectangle:
    """ This class represents
    a rectangle
    """
    
    def __init__(self, width=0, height=0):
        """ Initialises a new rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ This method returns the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ this class metd instantiates a width for
        a rectngle object
        """

        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This method returns the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ this class methd sets the value of the rectangle object to the
        supplied argument.
        """

        if not(isinstance(height, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
