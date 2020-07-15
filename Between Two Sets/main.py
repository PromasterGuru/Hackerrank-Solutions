def getTotalX(a, b):
    temp = []
    final = []
    i = a[len(a) - 1]
    while(i <= b[0]):
        isFactor = True
        for j in a:
            if(i%j != 0):
                isFactor = False
        if(isFactor):
            temp.append(i)
        isFactor = True
        i += a[len(a) - 1]
    for i in range(len(temp)):
        found = True
        for j in b:
            if(j%temp[i] != 0):
                found = False
        if(found):
            final.append(temp[i])
    return len(final)

if __name__=="__main__":
    arr1 = [2,4]
    arr2 = [16, 32, 96]
    print(getTotalX(arr1, arr2))