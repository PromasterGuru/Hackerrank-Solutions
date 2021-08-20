import math
def encryption(s):
    s = s.replace(" ","")
    r = math.floor(math.sqrt(len(s)))
    c = math.ceil(math.sqrt(len(s)))
    encryptedS = ""
    i = 0
    while i < c:
        j = i
        while j < len(s):
            encryptedS += s[j]
            j += c
        i += 1
        encryptedS += " "
    return encryptedS
        
if __name__ == "__main__":
    s = "have a nice day"
    s = "feedthedog"
    s = "chillout"
    print(encryption(s))
