#!/usr/bin/python3
"""Defines Write_file module."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file.
    """
    with open(filename, "W", encoding="utf-8") as my_file:
        return my_file.write(text)
