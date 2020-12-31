# def solution(k, A):
#     counter = 0
#     ar = sorted(A)
#     for i in range(len(ar) - 1, -1,-1):
#         if ar[i] != 0:
#             j = i
#             counter += 1
#             while(ar[j] == ar[j-1]):
#                 counter += 1
#                 j -= 1
#             if counter >= k:
#                 return counter
#     return counter

# print(solution(3, [100,50,50,50,50,25]))
# print(solution(4, [20,40,60,100]))
# print(solution(4, [2,2,3,4,5]))
# print(solution(4, [20,40,60,80,100,0]))
# print(solution(2, [2,2,3,4,5]))

from itertools import product
def solution(a, x):
    ar = [[a[i],a[j]] for i in range(len(a)) for j in range(i+1, len(a))]
    arr = []
    for a in ar:
        arr.append(min(a))
    return max(arr)
    



print(solution([8,2,4,2], 2))

