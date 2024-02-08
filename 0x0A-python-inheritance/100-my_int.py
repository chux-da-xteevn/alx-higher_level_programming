#!/usr/bin/python3
"""class Myint that inherits from int."""


class Myint(int):
    """Myint class body"""

    def __eq__(self, value):
        """Överride == opeartor with !=."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with ==."""
        return self.real == value
