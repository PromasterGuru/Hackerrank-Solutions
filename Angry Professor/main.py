#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    early_students = 0
    for i in a:
        if i <= 0:
            early_students += 1
        if early_students >= k:
            return "NO"
    return "YES"
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
