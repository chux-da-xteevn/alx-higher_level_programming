#!/usr/bin/python3
"""class to define square"""




class Square:
    """
    Representation of a Square.
    """

    def __init__(self, size=0):
        """

        the init function gets invoked whenever a new instance is created
        :param size:
        """


        if not ininstance(size, int):
            raise TypeError("aize must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
