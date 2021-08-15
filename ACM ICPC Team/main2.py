def acmTeam(topic):
    res = 0
    count = 0
    for i in range(len(topic) - 1):
        for j in range(i+1, len(topic)):
            tmp = bin(int(topic[i], 2) | int(topic[j], 2)).count("1")
            if tmp > res:
                count = 1
                res = tmp
            elif tmp == res:
                count += 1
    return [res, count]
        
if __name__ == "__main__":
    topic = ["10101","11100","11010","00101"]
    print(acmTeam(topic))