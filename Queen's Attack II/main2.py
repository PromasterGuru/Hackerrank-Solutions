def queensAttack(n, k, r_q, c_q, obstacles):
    obstacleMap = {(i,j): 0 for i,j in obstacles}
    possibleMoves = [[1,-1],[-1,1],[0,-1],[0,1],[-1,-1],[1,1],[1,0],[-1,0]]
    count = 0
    for move in possibleMoves:
        r = r_q + move[0]
        c = c_q + move[1]
        while (r >= 1 and r <= n) and (c >= 1 and c<= n) and (r,c) not in obstacleMap:
            r += move[0]
            c += move[1]
            count += 1
    return count

if __name__ == '__main__':
    n = 8
    k = 0
    r_q = 4
    c_q = 4
    obstacles = [[1,4],[2,2],[3,5]]
    print(queensAttack(n, k, r_q, c_q, obstacles))