"""
Module with for-loops that loop over positions.

Author: Juliet George
Date: 8/3/2020
"""


def skip(s,n): #for-loop
    """
    Returns a copy of s, only including positions that are multiples of n

    A position is a multiple of n if pos % n == 0.

    Examples:
        skip('hello world',1) returns 'hello world'
        skip('hello world',2) returns 'hlowrd'
        skip('hello world',3) returns 'hlwl'
        skip('hello world',4) returns 'hor'

    Parameter s: the string to copy
    Precondition: s is a nonempty string

    Parameter n: the letter positions to accept
    Precondition: n is an int > 0
    """

    s1 = ""
    for pos in range(len(s)):
        if pos%n == 0:
            s1 = s1 + str(s[pos])
    return s1


def skip(s,n): #while-loop
    """
    Returns a copy of s, only including positions that are multiples of n

    A position is a multiple of n if pos % n == 0.

    Examples:
        skip('hello world',1) returns 'hello world'
        skip('hello world',2) returns 'hlowrd'
        skip('hello world',3) returns 'hlwl'
        skip('hello world',4) returns 'hor'

    Parameter s: the string to copy
    Precondition: s is a nonempty string

    Parameter n: the letter positions to accept
    Precondition: n is an int > 0
    """
    # You must use a while-loop, not a for-loop
    l = len(s)
    start = 0
    res = ""
    while start < l:
        if start % n == 0:
            res = res + s[start]
        start = start + 1
    return res
