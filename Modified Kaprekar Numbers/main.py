def isKaprekarNumber(num):
    if num < 4:
        return num == num ** 2
    strSq = str(num**2)
    n = len(strSq)//2
    return num == (int(strSq[:n]) + int(strSq[-(len(strSq) - n):]))
        
def kaprekarNumbers(p, q):
    valid_range = False
    for num in range(p, q+1):
        if isKaprekarNumber(num):
            valid_range = True
            print(num, end=" ")
    if not valid_range:
        print("INVALID RANGE")

if __name__ == "__main__":
    # kaprekarNumbers(100, 300)
    # kaprekarNumbers(1, 100)
    kaprekarNumbers(40, 43)