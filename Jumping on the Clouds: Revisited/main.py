#!/bin/python

import math
import os
import random
import re
import sys


def calculateEnergy(n):
    return 1 if n == 0 else 3


def jumpingOnClouds(c, k):
    ar = list(c)
    energy = 100
    i = 0
    while((i+k) % n != 0):
        energy -= calculateEnergy(ar[(i+k) % n])
        i += k
    return (energy - calculateEnergy(ar[0]))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, k = map(int, input().split())

    c = map(int, input().rstrip().split())

    result = jumpingOnClouds(c, k)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()

"""
10 3
1 1 1 0 1 1 0 0 0 0
80
"""
