def twoSum(nums, target):
    numMap = {}
    for i, n in enumerate(nums):
        if target - n in numMap:
            return [numMap[target - n], i]
        numMap[n] = i


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4, 15], 6))
    print(twoSum([3, 3], 6))
