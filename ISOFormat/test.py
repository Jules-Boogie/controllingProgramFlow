"""
A test script for the function iso_8601.

Author: Juliet George
Date: July 31, 2020
"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')

    # Put your test cases here
    result = func.iso_8601('02:44:02')
    introcs.assert_equals(True, result)

    result = func.iso_8601('25:44:02')
    introcs.assert_equals(False, result)

    result = func.iso_8601('23:70:02')
    introcs.assert_equals(False, result)

    result = func.iso_8601('23:55:63')
    introcs.assert_equals(False, result)

    result = func.iso_8601('13:40:2')
    introcs.assert_equals(False, result)

    result = func.iso_8601('13:4:20')
    introcs.assert_equals(False, result)

    result = func.iso_8601(',:40:20')
    introcs.assert_equals(False, result)

    result = func.iso_8601('13:40:,')
    introcs.assert_equals(False, result)

    result = func.iso_8601('11:,:20')
    introcs.assert_equals(False, result)

    result = func.iso_8601('3:40:20')
    introcs.assert_equals(True, result)



if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')
