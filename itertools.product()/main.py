from itertools import product
A = [int(i) for i in input().split(' ')]
B = [int (j) for j in input().split(' ')]
for t in product(sorted(A), sorted(B)):
    print(t, end=" ")