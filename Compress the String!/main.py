from itertools import groupby
print(*[(len(list(g)), int(k)) for k,g in groupby(input())])