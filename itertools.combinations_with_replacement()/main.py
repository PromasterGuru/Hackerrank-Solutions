from itertools import combinations_with_replacement
line = input().split()
for it in combinations_with_replacement(sorted(line[0]), int(line[1])):
    print(''.join(it))
