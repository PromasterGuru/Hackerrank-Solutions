import string
import random


def minion_game(s):
    kevin = 0
    stuart = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(s)):
        if s[i] in vowels:
            kevin += (len(s) - i)
        else:
            stuart += (len(s) - i)

    if kevin > stuart:
        print("Kevin {}".format(kevin))
    elif stuart > kevin:
        print("Stuart {}".format(stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    # s = input()
    # s = 'BANANA'
    s = ''.join(random.choice(string.ascii_uppercase)for i in range(1000000))
    minion_game(s)

'''
B
N
BA
BAN
BANA
BANANA

A
AN
ANA
ANAN
ANANA

N
NA
NAN
NANA


'''
