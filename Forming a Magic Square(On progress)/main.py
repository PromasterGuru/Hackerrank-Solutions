def formingMagicSquare(s):
    cost = 0
    #Fix diagnols
    for x,ar in enumerate(s):
        d = abs(15 - sum(ar))
        if d > 0:
            m = max(ar)
            for y,j in enumerate(ar):
                if j ==m:
                    cost += abs(j-d)
                    print(x,y)
                    s[x][y] = d
    print(s)
    
    return cost

    
if __name__ == "__main__":
    s = [
        [5, 3, 4],
        [1, 5, 8],
        [6, 4, 2]
    ]

    s = [
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

    """
    [2 9 4]
    [7 5 3]
    [6 1 8]

    [6 7 2]
    [1 5 9]
    [8 3 4]

    [4 9 2]
    [3 5 7]
    [8 1 6]

    [8 1 6]
    [3 5 7]
    [4 9 2]

    [6 1 8]
    [7 5 3]
    [2 9 4]

    (0,0) -> (0,1)(0,2)(2,2)
    (1,1) -> (1,2)
    (0,2) -> (0,0)(2,2)(0,1)
    (1,2) -> (1,0)
    (2,2) -> (0,0)(0,2)(1,2)
    """
