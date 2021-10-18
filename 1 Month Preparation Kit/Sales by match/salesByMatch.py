#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(ar):
    # Write your code here
    print(sum([ar.count(value)//2 for value in set(ar)]))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #ar = list(map(int, input().rstrip().split()))

    result = sockMerchant([10,20,20,10,10,30,50,10,20])

    #fptr.write(str(result) + '\n')

    #fptr.close()
