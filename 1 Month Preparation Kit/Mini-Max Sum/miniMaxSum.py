import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max_value = max(arr)
    min_value = min(arr)

    if max_value > 10^9:
        return

    if min_value < 1:
        return

    aux_arr = arr.copy()
    arr.remove(max_value)
    aux_arr.remove(min_value)
    
    print(str(sum(arr)) + ' ' + str(sum(aux_arr)))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)