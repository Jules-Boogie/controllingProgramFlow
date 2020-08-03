"""
Test script for the for-loop functions

Author: Walker M. White
Date: July 30, 2019
"""
import introcs
import func


def test_revrange():
    """
    Test procedure for function revrange().
    """
    print('Testing revrange()')

    result = funcs.revrange(0,3)
    introcs.assert_equals((2,1,0),result)

    result = funcs.revrange(0,4)
    introcs.assert_equals((3,2,1,0),result)

    result = funcs.revrange(5,10)
    introcs.assert_equals((9,8,7,6,5),result)

    result = funcs.revrange(3,3)
    introcs.assert_equals((),result)

if __name__ == '__main__':
    test_revrange()
    print('Module funcs passed all tests.')
