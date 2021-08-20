import math
def encryption(s):
    s = s.replace(" ","")
    c = math.ceil(math.sqrt(len(s)))
    c = math.ceil(math.sqrt(len(s)))
    encryptedS = ""
    for i in range(c):
        encryptedS += s[i::c] +" "
    return encryptedS
        
if __name__ == "__main__":
    s = "have a nice day"
    s = "feedthedog"
    s = "chillout"
    print(encryption(s))
