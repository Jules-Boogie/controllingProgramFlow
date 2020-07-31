"""
A function to search for the first vowel position

Author: Juliet George
Date: 7/30/2020
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.

    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.

    Examples:
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1

    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """

    result = len(s)
    vowels = ['a','e','i','o','u']
    for x in vowels:
        if x in s:
            result = min(result,introcs.find_str(s,x))
        if not x in s and "y" in s and introcs.rfind_str(s,"y") != 0:
            result = introcs.rfind_str(s,"y")
    return result if result != len(s) else -1
