def formingMagicSquare(s):
    cost = 0
    for a in s:
        for j in range(len(a)):
            print(a[j])

if __name__ == "__main__":
    s = [
        [5, 3, 4],
        [1, 5, 8],
        [6, 4, 2]
    ]

    s= [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 5]
    ]

    s = [
        [4, 8, 2],
        [4, 5, 7],
        [6, 1, 6]
    ]
    print(formingMagicSquare(s))