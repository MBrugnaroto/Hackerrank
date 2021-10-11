#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    result_str = ""
    result = []
    n = len(arr)
    
    for index in range(n):
        result.append(0)
        
    for index in range(n):
        if arr[index] >= n:
            return
        result[arr[index]] += 1
    
    for index in range(100):
        result_str += str(result[index]) + ' '
    
    print(result_str)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
