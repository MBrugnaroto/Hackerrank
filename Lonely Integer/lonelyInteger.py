#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    
    dic = {}

    for key in a:
        dic[key] = 0

        for item in a:
            if key == item:
                dic[key] = dic[key] + 1

    result = min(dic, key=dic.get) if dic[min(dic, key=dic.get)] == 1 else ""
    return result 

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(lonelyinteger(a))
