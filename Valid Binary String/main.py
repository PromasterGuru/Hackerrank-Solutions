def minimumMoves1(s, d):
    count = 0
    i = 0
    while(i < len(s)):
        if(s[i] == "0"):
            if("1" in s[i:]):
                pos = s[i:].index("1")
                count += len(s[i:i+pos])//d
                i += pos
            else:
                count += len(s[i:])//d
                i += len(s)
        else:
            i+=1
    return count
    

def minimumMoves2(s, d):
    target = '0'*d
    return s.count(target)

if __name__ == "__main__":
    d = 5
    s = "1111100100"
    s = "00100"
    s = "111"*1000000
    s = "000000000"
    # s = "1111100011100001110010"
    print(minimumMoves1(s,d))
    print(minimumMoves2(s,d))