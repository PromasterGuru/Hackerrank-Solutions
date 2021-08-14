def commonChild(s1, s2):
    s1Map = {}
    s2Map = {}
    for i in range(len(s1)):
        if s1[i] in s1Map:
            s1Map[s1[i]].append(i)
        else:
            s1Map[s1[i]] = [i]
        if s2[i] in s2Map:
            s2Map[s2[i]].append(i)
        else:
            s2Map[s2[i]] = [i]
    s1c = len(s1)
    s2c = len(s2)
    s1MapD = {}
    s2MapD = {}
    res1 = ""
    res2 = ""
    for j in range(len(s1)):
        if s1[j] in s1Map and s1[j] in s2Map and (s1Map[s1[j]][0] + s2Map[s1[j]][0]) < s1c:
            s1c = s2Map[s1[j]][0]
        if s2[j] in s1Map and s2[j] in s2Map and (s1Map[s2[j]][0] + s2Map[s2[j]][0]) < s2c:
            s2c = s1Map[s2[j]][0]
    print(s1c, s2c)
    while s1c < len(s1):
        print(s2Map)
        if s1[s1c] in s2Map:
            res1 += s1[s1c]
            if len(s2Map[s1[s1c]]) == 0:
                del s2Map[s1[s1c]]
            else:
                s2MapD[s1[s1c]] = s2Map[s1[s1c]][0]
                s2Map[s1[s1c]].pop(0)
        s1c += 1
    while s2c < len(s2):
        if s2[s2c] in s1Map:
            res2 += s2[s2c]
            del s1Map[s2[s2c]]
        s2c += 1

    return res1



if __name__ == '__main__':
    s1 = "HALRY"
    s2 = "SALLY"
    s1 = "AA"
    s2 = "BB"
    s1 = "SHINCHAN"
    s2 = "NOHARAAA"
    s1 = "ABCDEF"
    s2 = "FBDAMN"
    s1 = "ABCDEFBDA"
    s2 = "FBDAMNSDR"
    print(commonChild(s1,s2))
