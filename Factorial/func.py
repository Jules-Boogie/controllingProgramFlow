"""
Module with range-based for-loop functions.

Author: Juliet George
Date: 8/2/2020
"""

def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1

    0! is 1.  Factorial is undefined for integers < 0.

    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120

    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    result = 1
    for x in range(1,n+1):
        result *= x
    return result
