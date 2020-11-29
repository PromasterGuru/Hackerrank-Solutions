import math
import os
import random
import re
import sys


T = int(input().strip())
arr = []
for i in range(T):
    arr.append(0)
    n , k = map(int , input().split())
    arr[i] = k-1 if ((k-1) | k) <= n else k-2
print(*arr, sep='\n')