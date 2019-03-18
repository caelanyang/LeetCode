def two_sum(nums, target):
    for i, a in enumerate(nums):
        for j in range(i + 1, len(nums)):
            b = nums[j]
            if a + b == target:
                return [i, j]
    else:
        print("No two sum for target %d" % target)
        return [-1, -1]


def main():
    nums = [2, 7, 11, 15]
    result = two_sum(nums, 26)
    print(result)


main()
