nums = [2, 7, 11, 15]
target = 9

nums_map = {}

for idx, num in enumerate(nums):
    if target-num in nums_map:
        print([nums_map[target-num], idx])

    nums_map[num] = idx

