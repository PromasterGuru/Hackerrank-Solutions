from itertools import permutations
K, M = map(int, input().split(" "))
numlist = []
s_max = 0
for a in range(K):
    arr = list(map(int, input().split(" ")))[1:]

    if not numlist:
        numlist = arr
    else:
        numlist = [y+[x] if isinstance(y, list) else [x, y]
                   for x in arr for y in numlist]
for ar in numlist:
    s = 0
    if not isinstance(ar, list):
        s = ar**2
    else:
        for j in ar:
            s += j**2
    if s % M > s_max:
        s_max = s % M
print(s_max)
