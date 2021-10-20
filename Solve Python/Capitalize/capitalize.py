#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    result = []
    
    for word in words:
        if word == '':
            result.append(word)
        else:
            word = list(word)
            word[0] = word[0].upper()
            result.append(''.join(word))
        
    print(' '.join(result))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    #fptr.write(result + '\n')

    #fptr.close()
