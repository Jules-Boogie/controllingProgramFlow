"""
A function to check the validity of a numerical string

Author: Juliet George
Date: July 30th, 2020
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.

    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.

    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).

    Examples:
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False

    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    #digits and commas
    #commas after 3 digits

    result = False
    valid = ("0123456789,")
    invalid =("-;:@!#abcdefghijklmnopqrstuvwxyz")
    paramlength = len(s)
    params = introcs.split(s)
    if s == '0':
        result = True
    elif paramlength <= 3 and "0" != s[0] and "," not in s:
        for x in params:
            if introcs.rfind_str(valid,x):
                result = True
        for x in s:
            if x in invalid:
                result = False
    elif paramlength >= 4 and "0" != s[0]:
        if "," in s:
            first, last_part = s.split(",")
            if len(last_part) == 3 and len(first) >= 1:
                result = True
            else:
                result = False
        else:
            result = False
        for x in s:
            if x in invalid:
                result = False
    return result
