import math
import pdb
def counterGame(n):
    players = ['Louise', 'Richard']
    player = False #False is equivalent to zero, index of the first player
    while(n > 1):
        p = int(math.log(n)/math.log(2))
        value = 2**p
        if(value == n):
            n /= 2
        else:
            n -= value
        if(n > 1):
            player = not player
    return players[player]

if __name__ == "__main__":
    n = 132
    print(counterGame(n))
