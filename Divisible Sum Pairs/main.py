
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i,n):
            if(i < j and (ar[i] + ar[j])%k==0):
                print(ar[i], ar[j])
                count += 1
    return count

if __name__ == "__main__":
    n = 5
    k = 6
    ar = [1,2,3,4,5,6]

    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]
    print(divisibleSumPairs(n, k, ar))

