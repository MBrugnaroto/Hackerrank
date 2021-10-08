#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    delimiter = r'P|p|A|a'

    try:
        time = re.search(delimiter, s).start()    
    except:
        return

    try:
        split_clock = re.search(':', s).start()
    except:
        split_clock = time

    if s[time:time+2] == 'PM':
        convert = (0 if int(s[:int(split_clock)]) == 12 else int(s[:int(split_clock)])) + 12
        s = str(convert) + s[int(split_clock):time]
        print(s)

    if s[time:time+2] == 'AM':
        convert = ('00' if int(s[:int(split_clock)]) == 12 else s[:int(split_clock)])
        s = convert + s[int(split_clock):time]
        print(s)
    
if __name__ == '__main__':
    s = input()

    result = timeConversion(s)