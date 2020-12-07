import string


def print_rangoli(size):
    alphabets = list(string.ascii_lowercase)[:size]
    for i in range(size-1, -size, -1):
        res = '-'.join(alphabets[size-1:abs(i):-1] + alphabets[abs(i):size])
        print(res.center(4*size-1, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
