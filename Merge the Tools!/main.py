def merge_the_tools(string, k):
    counter = 1
    charMap = {}
    for c in string:
        if c not in charMap:
            print(c, end="")
            charMap[c] = 1
        if(counter % k == 0):
            print("")
            charMap = {}
        counter += 1


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
