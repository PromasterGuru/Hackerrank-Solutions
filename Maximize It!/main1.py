from itertools import product

K, M = map(int, input().split())
print(max(map(lambda x: sum(i**2 for i in x)%M, product(*[list(map(int, input().split()))[1:] for _ in range(K)]))))
