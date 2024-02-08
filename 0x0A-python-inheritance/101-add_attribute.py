#!/usr/bin/python3
"""Defines a function attribute."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.
    Raises:
        TypeError: if the attribute cannot be added.
    """
    if not hasattr(obj, "__dict"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
