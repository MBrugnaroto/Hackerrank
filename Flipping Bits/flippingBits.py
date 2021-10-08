#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here

    convert_to_binary = '{:032b}'.format(n)
    binary = ""

    for character in convert_to_binary:
        binary += '1' if character == '0' else '0'

    decimal = int(binary, 2)
    print(decimal)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)
