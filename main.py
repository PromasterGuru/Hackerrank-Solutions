def fibonacci(n):
    # if n == 0:
    #     return 1
    # else:
    #     return n * fibonacci(n-1)
    # n = 0
    # m = 1
    # for _ in range(s):
    #     temp = m
    #     m += n
    #     n = temp
    # print(n)
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    print(fibonacci(9))
