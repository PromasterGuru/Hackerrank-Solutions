def gradingStudents(grades):
    for i in range(len(grades)):
        if(grades[i] >=38 and grades[i] % 5 >= 3):
            grades[i] = (grades[i]//5 * 5) + 5
    return grades

if __name__ == '__main__':
    arr = [73, 67, 38, 33]
    print(gradingStudents(arr))