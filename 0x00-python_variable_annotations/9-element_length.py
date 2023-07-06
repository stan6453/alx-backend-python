#!/usr/bin/env python3
"""  Annotate the below function’s parameters and return values with
the appropriate types """


from typing import Callable


def element_length(lst):
    """  Annotate this function’s parameters and return values with
    the appropriate types """
    return [(i, len(i)) for i in lst]
