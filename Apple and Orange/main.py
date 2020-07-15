def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(len([d for d in apples if (d + a) >= s and (d + a) <= t]))
    print(len([d for d in oranges if (b + d) <= t and (b + d) >= s]))

if __name__=="__main__":
    countApplesAndOranges(7,11,5,15,[-2, 2, 1],[5, -6])