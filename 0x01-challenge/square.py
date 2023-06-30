#!/usr/bin/python3
""" This module contains a class Square """

class Square():
    """ This class defines a square """

    def __init__(self, *args, **kwargs):
        """ Initializes the square """
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Returns the area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Returns the perimeter of the square """
        return self.width * 4

    def __str__(self):
        """ Returns the dimensions of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
