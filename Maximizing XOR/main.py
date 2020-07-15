def maximizingXor(l, r):
    max_xor = 0
    for i in range(l,r+1):
        for j in range(i, r+1):
            if(i^j > max_xor):
                max_xor = i^j
    return max_xor
if __name__ == "__main__":
    l = 11
    r = 100
    print(maximizingXor(l, r))