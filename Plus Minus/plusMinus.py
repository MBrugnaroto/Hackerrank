#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    dic = {
        'Positive': 0,
        'Negative': 0,
        'Zero': 0
    }

    for value in arr:
        if value < -100 or value > 100:
            return
        if value > 0:
            dic['Positive'] = dic['Positive'] + 1
        elif value == 0:
            dic['Zero'] = dic['Zero'] + 1
        else:
            dic['Negative'] = dic['Negative'] + 1

    for key in dic:
        print("{:.6f}".format(dic[key]/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    if 0 < n <= 100:
        plusMinus(arr)