def utopianTree(n):
    height = 1
    for i in range(n):
        if(height % 2 ==0):
            height += 1
        else:
            height *= 2
    return height

if __name__ == "__main__":
    n = 3
    print(utopianTree(n))