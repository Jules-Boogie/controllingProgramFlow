"""
Module with range-based for-loop functions.

Author: Juliet George
Date: 8/2/2020
"""

def revrange(a,b):
    """
    Returns the tuple (b-1, b-2, ..., a)

    Note that this tuple is the reverse of tuple(range(a,b))

    Parameter a: the "start" of the range
    Precondition: a is an int <= b

    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """
    result = ()
    for x in range(a,b):
        result = (x,) + result
    return result
