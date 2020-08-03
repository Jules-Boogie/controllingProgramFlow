"""
Module with for-loops that loop over positions.

Author: Juliet George
Date: 8/3/2020
"""


def fixed_points(tup): #for-loop
    """
    Returns a copy of tup, including only the "fixed points".

    A fixed point of a tuple is an element that is equal to its position in the tuple.
    For example 0 and 2 are fixed points of (0,3,2).  The fixed points are returned in
    the order that they appear in the tuple.

    Examples:
        fixed_points((0,3,2)) returns (0,2)
        fixed_points((0,1,2)) returns (0,1,2)
        fixed_points((2,1,0)) returns ()

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of ints
    """
    fixed_point = ()
    for pos in  range(len(tup)):
        if pos == tup[pos]:
            fixed_point = fixed_point + (tup[pos],)
    return fixed_point


def fixed_points(tup): #while-loop
    """
    Returns a copy of tup, including only the "fixed points".

    A fixed point of a tuple is an element that is equal to its position in the tuple.
    For example 0 and 2 are fixed points of (0,3,2).  The fixed points are returned in
    the order that they appear in the tuple.

    Examples:
        fixed_points((0,3,2)) returns (0,2)
        fixed_points((0,1,2)) returns (0,1,2)
        fixed_points((2,1,0)) returns ()

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of ints
    """
    # You must use a while-loop, not a for-loop
    res = ()
    l = len(tup)
    start = 0
    while start < l:
        if start == tup[start]:
            res = res + (tup[start],)
        start = start + 1
    return res
