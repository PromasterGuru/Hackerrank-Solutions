def reverseWords(s):
    rev_string = s.split(" ")
    arr = []
    for i in range(len(rev_string) - 1, -1, -1):
        word = rev_string[i].strip()
        if bool(word and word.strip()):
            arr.append(word.strip())
    return " ".join(arr)


if __name__ == "__main__":
    s = " the sky is  blue "
    print(reverseWords(s))
