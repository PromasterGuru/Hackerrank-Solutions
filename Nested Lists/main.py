if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        arr.append([input(), float(input())])
    second_highest = sorted(list(set([marks for name, marks in arr])))[1]
    print(*[name for name, score in sorted(arr) if score == second_highest], sep='\n')
