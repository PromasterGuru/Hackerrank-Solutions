from itertools import permutations
a,n = input().split(" ")
for a in sorted(list(permutations(a,int(n)))):
    print("".join(a))