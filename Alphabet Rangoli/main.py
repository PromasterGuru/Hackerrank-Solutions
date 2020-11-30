import string


def print_rangoli(size):
    alphabets = list(string.ascii_lowercase)[:size]
    i = size - 1
    dashes = '-'*2*i
    print("{}{}{}".format(dashes, alphabets[i], dashes))
    if(len(alphabets) > 1):
        while i > 0:
            i -= 1
            dashes = '-'*2*i
            print("{}{}-{}{}".format(dashes,
                                     '-'.join(reversed(alphabets[i+1:size])), '-'.join(alphabets[i:size]), dashes))

        i = 0
        while i < size-2:
            i += 1
            dashes = '-'*2*i
            print("{}{}-{}{}".format(dashes,
                                     '-'.join(reversed(alphabets[i:size])), '-'.join(alphabets[i+1:size]), dashes))
        i = size - 1
        dashes = '-'*2*i
        print("{}{}{}".format(dashes,
                              alphabets[i], dashes))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
