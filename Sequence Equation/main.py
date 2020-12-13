#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def permutationEquation(p):
    return [p.index(p.index(p.index(i)+1)+1)+1 for i in p]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
