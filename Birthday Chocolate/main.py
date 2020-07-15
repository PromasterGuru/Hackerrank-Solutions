def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if(sum(s[i: i+m]) == d):
            count += 1
    return count

if __name__ == '__main__':
    d = 4
    m = 1
    s = [4]
    print(birthday(s, d, m))