def organizingContainers(containers):
    ballsByColor = [0]*len(containers)
    ballsPerContainer = [0]*len(containers)
    for i in range(len(containers)):
        for j in range(len(containers)):
            ballsPerContainer[i] += containers[i][j]
            ballsByColor[j] += containers[i][j]
    ballsByColor.sort()
    ballsPerContainer.sort()
    for n in range(len(containers)):
        if ballsByColor[n] != ballsPerContainer[n]:
            return "Impossible"
    return "Possible"

if __name__ == "__main__":
    containers= [[1,3,1],[2,1,2],[3,3,3]]
    containers = [[0,2,1],[1,1,1],[2,0,0]]
    containers = [[1,1],[1,1]]
    containers = [[0,2],[1,1]]
    containers = [[9,2,1],[2,0,0],[1,1,1]]
    print(organizingContainers(containers))
    
    