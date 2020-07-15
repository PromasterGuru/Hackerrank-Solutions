# from itertools import combinations
from itertools import groupby
def minion_game(string):
    stuart = 0
    kevin = 0
    s = ['A','E','O','U']
    # for i in range(1, len(string) + 1):
    #     for s in groupby(string):
    #         print(s)
    for k,g in groupby(string):
        print(k,list(g))
            
if __name__ == '__main__':
    s = input()
    minion_game(s)