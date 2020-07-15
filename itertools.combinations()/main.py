from itertools import combinations
if __name__=='__main__':
    line = input().split()
    S = sorted(line[0])
    k = int(line[1])
    for i in range(1, k + 1):
        for a in combinations(S, i):
            print(''.join(a))
