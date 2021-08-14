#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
from collections import Counter
def nonDivisibleSubset(k, s):
    c = Counter(i%k for i in s)
    count = 0
    blacklist = set()
    for x,y in c.most_common():
        if x == k/2 or x == 0:
            count += 1
        elif k - x not in blacklist:
            count += y
            blacklist.add(x)
    return count
                     
                        
if __name__ == '__main__':
    k = 4
    s = [1, 7, 2, 4]
    s = [19, 10, 12, 10, 24, 25, 22]
    s = [2, 3, 4, 5]
    print(nonDivisibleSubset(k, s))