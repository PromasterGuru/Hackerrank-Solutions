def pageCount(n, p):
    if n % 2 > 0:
        return p//2 if n//2 >= p else (n-p)//2
    else:
        return p//2 if n//2 >= p else (n+1-p)//2


if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    print(result)
