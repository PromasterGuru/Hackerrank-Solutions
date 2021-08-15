def acmTeam(topic):
    topicMap = []
    scoreMap = {}
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            topicMap.append([topic[i], topic[j]])
    
    for mp in topicMap:
        count = 0
        for n in range(len(mp[0])):
            if mp[0][n] == "1" or mp[1][n] == "1":
                count += 1
        if count in scoreMap:
            scoreMap[count] += 1
        else:
            scoreMap[count] = 1
    maximal = max(scoreMap) 
    return [maximal,scoreMap[maximal]]

if __name__ == "__main__":
    topic = ["10101","11100","11010","00101"]
    print(acmTeam(topic))