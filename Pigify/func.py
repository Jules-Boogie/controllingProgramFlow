"""
A collection of functions to support the translation of words into Pig Latin.

This module contains two functions.  The first function searchs for the location of the
first vowel.  The second function uses this as a helper to perform the conversion.

Author: Juliet George
Date: July 30th, 2020
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
            result = min(result,introcs.rfind_str(s,"y"))
    return result if result != len(s) else -1


def pigify(s):
    """
    Returns a copy of s converted to Pig Latin

    Pig Latin is childish encoding of English that adheres to the following rules:

    1.  The vowels are 'a', 'e', 'i', 'o', 'u', as well as any 'y'
        that is not the first letter of a word. All other letters are consonants.

        For example, 'yearly' has three vowels  ('e', 'a', and the last 'y')
        and three consonants (the first 'y', 'r', and 'l').

    2.  If the English word begins with a vowel, append 'hay' to the end of the word
        to get the Pig Latin equivalent. For example, 'ask 'askhay' and 'use' becomes
        'usehay'.

    3.  If the English word starts with 'q', then it must be followed by'u'; move
        'qu' to the end of the word, and append 'ay'.  Hence 'quiet' becomes
        'ietquay' and 'quay' becomes 'ayquay'.

    4.  If the English word begins with a consonant, move all the consonants up to
        the first vowel (if any) to the end and add 'ay'.  For example, 'tomato'
        becomes 'omatotay', 'school' becomes 'oolschay'. 'you' becomes 'ouyay' and
        'ssssh' becomes 'sssshay'.

    Parameter s: the string to change to Pig Latin
    Precondition: s is a nonempty string with only lowercase letters. If s starts with
    'q', then it starts with 'qu'.
    """

    test = first_vowel(s)
    if test == 0:
        result = s + 'hay'

    if s[0] == 'q':
        second = s[2:]
        result = second + "quay"

    elif s[0] != 'q' and test > 0:
        first = s[:test]
        second = s[test:]
        result = second + first + 'ay'

    elif s[0] != 'q' and test == -1:
        result = s + 'ay'

    return result
    
