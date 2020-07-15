def strangeCounter(t):
    initial = 3
    col = 1
    value = 0
    while(True):
        if(t > (col * 2)+1):
            initial =initial * 2
            col = initial - 2
        else:
            value = initial - (t - col)
            break
    return value
if __name__ == "__main__":
    t = 17
    print(strangeCounter(t))
