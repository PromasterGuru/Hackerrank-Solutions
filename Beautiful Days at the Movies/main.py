#!/bin/python3

import math
import os
import random
import re
import sys


def reverse(n):
    rev_num = 0
    while(n > 0):
        rev_num = (rev_num*10) + (n % 10)
        n //= 10
    return rev_num


def beautifulDays(i, j, k):
    days = 0
    for x in range(i, j+1):
        if abs(reverse(x) - x) % k == 0:
            days += 1
    return days


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
