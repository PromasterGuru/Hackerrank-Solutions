def hurdleRace(k, height):
    potions = 0
    max = k
    for i in height:
        if(i > max):
            potions += i - max
            max = i
    return potions
    

if __name__=="__main__":
    k = 2
    height = [2, 5, 4, 7, 2]
    print(hurdleRace(k, height))