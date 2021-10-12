#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    dic = {}
    aux = 1
    
    for querie in queries:
        if querie in dic.keys():
            dic[querie+str(aux*'*')] = 0
            aux+=1
        else:
            dic[querie] = 0
            
    for key in dic:
        if 1 > len(key) > 20:
            return 
        
        for string in strings:
            if 1 > len(string) > 20:
                return 
            if re.match('('+key.split('*', 1)[0]+')$', string):
                dic[key] = dic[key] + 1
                
    return dic.values()
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    if (1 <= strings_count <= 1000) and (1 <= queries_count <= 1000):
        res = matchingStrings(strings, queries)

        fptr.write('\n'.join(map(str, res)))
        fptr.write('\n')

        fptr.close()