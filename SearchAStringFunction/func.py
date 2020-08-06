"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Juliet George
Date: 8/5/2020
"""
import introcs


def findall(text,sub):
    """
    Returns the tuple of all positions of substring sub in text.

    If sub does not appears anywhere in text, this function returns the empty tuple ().

    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)

    Parameter text: The text to search
    Precondition: text is a string

    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    result = ()
    start = 0
    l = len(sub)
    while start < len(text):
        print(str(start) + "first")
        if (sub in text) and (text.find(sub,start,start+l+1) != -1):
            start = (text.find(sub,start,start+l+1))
            result = result + (start,)
        start = start + 1
        print(str(start) + "end")
    return result
