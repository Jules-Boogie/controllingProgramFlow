"""
A module to demonstrate how to test precondition enforcement.

This module has a function (and a helper) that uses assert statements to enforce
the preconditions.

Author: Juliet George
Date: July 31, 2020
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a string in 12-format <hours>:<min> AM/PM

    Example:
        valid_format('2:45 PM') returns True
        valid_format('2:45PM') returns False
        valid_format('14:45') returns False
        valid_format('14:45 AM') returns False
        valid_format(245) returns False

    Parameter s: the candidate time to format
    Precondition: NONE (s can be any value)
    """
    if type(s) != str:
        return False

    colon = introcs.find_str(s,':')
    if colon == -1:
        return False
    elif not introcs.isdigit(s[:colon]) or not introcs.isdigit(s[colon+1:colon+3]):
        return False

    hrs  = int(s[:colon])
    mins = int(s[colon+1:colon+3])
    if hrs < 1 or hrs > 12 or mins >= 60:
        return False

    return s[colon+3:] == ' AM' or s[colon+3:] == ' PM'


def time_to_minutes(s):
    """
    Returns the number of minutes since midnight

    Examples:
       time_to_minutes('2:45 PM') returns 885
       time_to_minutes('9:05 AM') returns 545
       time_to_minutes('12:00 AM') returns 0

    Parameter s: string representation of the time
    Precondition: s is a string in 12-format '<hours>:<min> AM/PM'
    """

    assert valid_format(s) == True
    #find the positions
    pos1 = introcs.find_str(s,":")
    pos2 = introcs.find_str(s," ")

    hour = str(s[:pos1])
    time = s[pos2+1:]
    currMin = int(s[pos1+1:pos2])

#     assert type(s) == str
#     assert 7 <= len(s) <= 8
#     assert currMin <= 60
#     assert 1 <= int(hour) <= 12
#     assert introcs.find_str(s,":") != -1
#     assert introcs.find_str(s," ") != -1





    # convert hour to minutes

    hour = str(s[:pos1])
    time = s[pos2+1:]
    currMin = int(s[pos1+1:pos2])
    if time == 'PM' and hour != '12':
        hour = int(hour)
        hour += 12
        min = int(hour) * 60
        currMin += min
    elif time == 'AM' and hour == '12':
        hour = 0
        min = int(hour) * 60
        currMin += min
    else:
        min = int(hour) * 60
        currMin += min
    return currMin




def str_to_minutes(s):
    """
    Returns the number of minutes since midnight.

    If s does not represent a time, this function returns -1.

    Examples:
       time_to_minutes('2:45 PM') returns 885
       time_to_minutes('9:05 AM') returns 545
       time_to_minutes('12:00 AM') returns 0
       time_to_minutes('12:75 AM') returns -1
       time_to_minutes('apple') returns -1

    Parameter s: a string potentially representating a time
    Precondition: s is non-empty
    """

    try:
        valid_format(s)
        result = time_to_minutes(s)
    except:
        result = -1

    return result
