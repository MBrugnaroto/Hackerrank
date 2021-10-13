#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    values = "not pangram" if len(set(re.findall('[a-z]', s.lower()))) < 26 else "pangram"
    
    print(values)

if __name__ == '__main__':
    s = input()

    result = pangrams(s)