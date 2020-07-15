def saveThePrisoner(n, m, s):
   rem = (m + s -1)
   if(rem <= n):
       return rem
   else:
       return (n if rem%n==0 else rem%n)
    
if __name__ == '__main__':

    n = 5
    m = 2
    s = 1
    print(saveThePrisoner(n, m, s))