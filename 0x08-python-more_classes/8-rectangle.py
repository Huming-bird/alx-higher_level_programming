#!/usr/bin/python3
""" This module is about a rectangle class """


class Rectangle:
    """ This class represents
    a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialises a new rectangle object"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This mtod returns the area of a rectangle object """
        return self.__width * self.__height

    def perimeter(self):
        """ This method reurns the perimeter of the rectangle object """
        if self.__width == 0 or self.__height == 0:
            per = 0
        else:
            per = 2 * (self.__width + self.__height)
        return per

    def __str__(self):
        """ This method returns the shsape of the rectangle object """
        strng = ''
        if self.__width == 0 or self.__height == 0:
            strng = ''
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    strng += str(self.print_symbol)
                if i != self.__height - 1:
                    strng += '\n'
        return strng

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not(isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not(isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() == max(rect_1.area(), rect_2.area()) else rect_2
