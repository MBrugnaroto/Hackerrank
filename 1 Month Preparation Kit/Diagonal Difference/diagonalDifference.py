#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonal_pri = len(arr)
    diagonal_sec = len(arr)
    total = 0

    for i in range(diagonal_pri):
        diagonal_sec = diagonal_sec - 1
        total += arr[i][i] - arr[i][diagonal_sec]
    
    print(abs(total))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
