# def solution(S):
#     occurrences = [0] * 26
#     for i in range(len(S)):
#         occurrences[ord(S[i]) - ord('a')] += 1
#     best_char = 'a'
#     best_res = 0
#     for i in range(26):
#         if(occurrences[i] == best_res and best_char > chr(ord('a') + i)):
#             best_char = chr(ord('a') + i)
#             best_res = occurrences[i]
#         elif occurrences[i] > best_res:
#             best_char = chr(ord('a') + i)
#             best_res = occurrences[i]
#     return best_char


# print(solution("hhheelllo"))

# def solution(file_object):
#     f = open(file_object, 'r')
#     nums = f.readlines()
#     for num in nums:
#         if str.isdigit(num.strip()):
#             yield num.strip().replace('+','').replace('-','')

# for n in set(solution("file.txt")):
#     print(n)

# def solution(A, B):
#     counter = 0
#     for i in range(1, len(A)):
#         if(sum(A[:i]) == sum(A[i:]) and sum(B[:i]) == sum(B[i:]) and (sum(A[:i]) == sum(B[i:]))):
#             counter += 1
#     return counter


# print(solution([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]))
# print(solution([4, -1, 0, 3], [-2, 6, 0, 4]))
# print(solution([3, 2, 6], [4, 1, 6]))
# print(solution([0, 4, -1,0,3], [0, -2, 5,0,3]))

# def solution(arr, target):
#     currencyMap = {}
#     rem = target
#     for i in arr:
#         if rem >= i:
#             currencyMap[i] = int(rem/i)
#             rem = round(rem % i, 2)
#     return currencyMap