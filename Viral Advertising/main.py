#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5
    cummurative = 0
    for _ in range(n):
        cummurative += (shared//2)
        shared = (shared//2) * 3
    return cummurative

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
