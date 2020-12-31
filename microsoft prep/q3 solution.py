def solution(A, B):
    lsumA = A[0]
    rsumA = sum(A[1:])
    lsumB = B[0]
    rsumB = sum(B[1:])
    counter = 0
    for i in range(1, len(A)):
        if lsumA == rsumA and lsumB == rsumB and lsumA == lsumB:
            counter += 1
        lsumA += A[i]
        rsumA -= A[i]
        lsumB += B[i]
        rsumB -= B[i]
    return counter

print(solution([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]))
print(solution([4, -1, 0, 3], [-2, 6, 0, 4]))
print(solution([3, 2, 6], [4, 1, 6]))
print(solution([0, 4, -1,0,3], [0, -2, 5,0,3]))