from typing import List
def shiftingLetters(s: str, shifts: List[int]) -> str:
    
    #SOLUTION 1
    res = ""
    j = len(s) - 1
    shift = 0
    while(j >= 0):
        shift += shifts[j]
        if((ord(s[j]) + shift%26)>ord('z')):
            res = chr(ord('a') + shift%26 - (ord('z') - ord(s[j])) - 1) + res
        else:
            res = chr(ord(s[j]) + (shift % 26)) + res
        j -= 1
    return res

    #SOLUTION 2
    a = ord('a')
    shift = 0
    res = ""
    for j in range(len(s) - 1, -1, -1):
        shift += shifts[j]
        res = chr((((ord(s[j]) - a + shift) % 26) + a)) + res
    return res
        
if __name__ == '__main__':
    s = "abc"
    shifts = [3,5,9]
    # s = "aaa"
    # shifts = [1,2,3]
    s = "ruu" 
    shifts = [26,9,17]
    
    # s = "ruu" 
    # shifts = [26,9,1]
    print(shiftingLetters(s, shifts))