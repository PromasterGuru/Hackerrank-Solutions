if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr, reverse=True)
    i = 1
    while(sorted_arr[i] == sorted_arr[0]):
        i+=1
    print(sorted_arr[i])
