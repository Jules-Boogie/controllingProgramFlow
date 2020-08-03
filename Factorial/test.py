"""
Test script for the for-loop functions

Author: Walker M. White
Date: July 30, 2019
"""
import introcs
import funcs


def test_factorial():
    """
    Test procedure for function factorial().
    """
    print('Testing factorial()')

    result = funcs.factorial(0)
    introcs.assert_equals(1,result)

    result = funcs.factorial(1)
    introcs.assert_equals(1,result)

    result = funcs.factorial(2)
    introcs.assert_equals(2,result)

    result = funcs.factorial(3)
    introcs.assert_equals(6,result)

    result = funcs.factorial(5)
    introcs.assert_equals(120,result)

    result = funcs.factorial(8)
    introcs.assert_equals(40320,result)

if __name__ == '__main__':
    test_factorial()
    print('Module funcs passed all tests.')
