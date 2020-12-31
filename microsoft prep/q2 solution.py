def solution(file_object):
    f = open(file_object, 'r')
    nums = f.readlines()
    for num in nums:
        try:
            yield int(num)
        except ValueError:
            pass

for n in solution("file.txt"):
    print(n)