import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    s = list(w)
    i = len(s) - 1
    while (i > 0 and s[i-1] >= s[i]):
        i -= 1
    if i <= 0:
        return "no answer"

    j = len(s) - 1
    while(s[j] <= s[i-1]):
        j -= 1
    s[i-1], s[j] = s[j], s[i-1]
    s[i:] = s[len(s) - 1: i - 1: -1]
    return "".join(s)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # T = int(input())

    # for T_itr in range(T):
    #     w = input()

    #     result = biggerIsGreater(w)
    #     print(result)

    # fptr.write(result + '\n')

    # fptr.close()

    arr = ["ab", "lmno", "dcba", "dcbb", "abdc", "abcd", "fedcbabcd"]
    # arr = ["ab","bb","hefg","dhck","dkhc"]
    # arr = ["dkhc"]
    # arr = ["dcba"]
    for w in arr:
        result = biggerIsGreater(w)
        print(result)

"""
ab
lmon
no answer
no answer
acbd
abdc
fedcbabdc
"""
