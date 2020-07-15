def arrangeStudents(b,g):
    x = sorted(b)
    y = sorted(g)
    i = 0
    while(i < len(x)-1):
        if((x[i] < y[i] and x[i+1] < y[i]) or (y[i] < x[i] and y[i+1] < x[i]) or (x[i] > y[i] and x[i+1] < y[i+1]) or (y[i] > x[i] and y[i+1] < x[i+1])):
            return "NO"
        i+=1
    return "YES"

if __name__ == "__main__":
    data = {
            1:[[5, 3, 8],[2, 4, 6]], 
            2:[[1,2],[3,4]], 
            3:[[1,3],[2,4]],
            4:[[1, 2, 4],[5, 6, 1]],
            5:[[1, 2, 4, 5],[6, 1, 3, 4]],
            6:[[2,1,3,4,5,9],[1,1,1,1,1,1]],
            7:[[1,2,5,4,2,2,2],[1,2,2,3,2,2,2]],
            8:[[1,3,3,5],[1,2,3,4]]
        }
    for i in data:
        a = data[i][0]
        b = data[i][1]
        print(arrangeStudents(a,b))






    a = [5, 3, 8]
    b = [2, 4, 6]

    a = [1,2]
    b = [3,4]

    a = [1,3]
    b = [2,4]

    a = [1, 2, 4]
    b = [5, 6, 1]

    a = [1, 2, 4, 5]
    b = [6, 1, 3, 4]

    a = [2,1,3,4,5,9]
    b = [1,1,1,1,1,1]


    # t1 = time.clock()
    # print(arrangeStudents1(a, b), Solution(a,b))
    # t2 = time.clock()

    # print("Time 2: ", (t2 - t1) * 1000)
