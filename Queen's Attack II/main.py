def queensAttack(n, k, r_q, c_q, obstacles):
    obstaclesMap = set()
    attacks = 0
    #Map obstacles
    for obstacle in obstacles:
        obstaclesMap.add((obstacle[0], obstacle[1]))
        
    #Horizontal-Left attacks
    for i in range(c_q-1, 0, - 1):
        if ((r_q, i) in obstaclesMap):
            break
        attacks += 1
        
    #Horizontal-Right attacks
    for i in range(c_q + 1, n+1):
        if ((r_q, i) in obstaclesMap):
            break
        attacks += 1
    
    #Vertical-Top attacks
    for i in range(r_q + 1, n+1):
        if ((i, c_q) in obstaclesMap):
            break
        attacks += 1
    
    #Vetical-Bottom attacks
    for i in range(r_q-1, 0, - 1):
        if ((i, c_q) in obstaclesMap):
            break
        attacks += 1
    
    #Diagonal-Left-Top attacks
    i = 1
    while ((c_q - i >= 1 and r_q + i <= n) and (r_q + i, c_q - i) not in obstaclesMap):
        attacks += 1
        i += 1
    
    #Diagonal-Right-Bottom attacks
    j = 1
    while ((r_q - j >= 1 and  c_q + j <= n) and (r_q - j, c_q + j) not in obstaclesMap):
        attacks += 1
        j += 1
        
    #Diagonal-Right-Top attacks
    x = 1
    while (((r_q + x) <= n and (c_q + x) <= n) and (r_q + x, c_q + x) not in obstaclesMap):
        attacks += 1
        x += 1
    
    #Diagonal-Left-Bottom attacks
    y = 1
    while (((r_q - y) >= 1 and (c_q - y) >= 1) and (r_q - y, c_q - y) not in obstaclesMap):
        attacks += 1
        y += 1
    return attacks

if __name__ == '__main__':
    n = 5
    k = 3
    r_q = 4
    c_q = 3
    obstacles = [[5,5],[4,2],[2,3]]
    
    n = 4
    k = 0
    r_q = 4
    c_q = 4
    obstacles = []
    
    n = 1
    k = 0
    r_q = 1
    c_q = 1
    obstacles = []
    
    n = 5
    k = 3
    r_q = 4
    c_q = 3
    obstacles = [[4,2],[4,4],[3,3],[5,3],[5,2],[3,4],[3,2],[5,4]]
    
    n = 8
    k = 0
    r_q = 4
    c_q = 4
    obstacles = [[1,4],[2,2],[3,5]]
    print(queensAttack(n, k, r_q, c_q, obstacles))
