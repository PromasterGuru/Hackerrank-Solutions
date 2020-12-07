def reverseWords(s):
   return ' '.join([word for word in s.strip().split(' ') if word != ''][::-1])

if __name__ == "__main__":
    s = " the sky is  blue "
    print(reverseWords(s))
