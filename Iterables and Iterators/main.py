from itertools import combinations
n = int(input())
a = input().split(" ")
k = int(input())
s = 0
counter = 0
for t in combinations(a,k):
    if 'a' in t:
        counter += 1
    s += 1
print(round(counter/s, 3))