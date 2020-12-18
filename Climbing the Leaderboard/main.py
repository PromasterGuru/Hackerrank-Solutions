#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    j = 0
    ar = []
    ranks = sorted(list(set(ranked)), reverse=True)
    for i in player[::-1]:
        while(j < len(ranks)):
            if i >= ranks[j]:
                ar.append(j+1)
                break
            j+=1
        if j == len(ranks):
            ar.append(j+1)
    return ar[::-1]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = 6  # int(input().strip())

    # list(map(int, input().rstrip().split()))
    ranked = [100, 90, 90, 80, 75, 60]

    player_count = 5  # int(input().strip())

    player = [50, 65, 77, 90, 102]  # list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

"""
6
100 90 90 80 75 60
5
50 65 77 90 102
"""
