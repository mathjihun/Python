import collections
from bisect import bisect_right, bisect_left

nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]

counter = collections.Counter(nums)
nums = sorted(counter)
ret = []
for i, num in enumerate(nums):
    if num == 0:
        if counter[num] > 2:
            ret.append([0, 0, 0])
    elif counter[num] > 1 and -2 * num in counter:
        ret.append([num, num, -2 * num])
    if num < 0:
        opposite = -num
        left = bisect_left(nums, opposite - nums[-1], i + 1)
        right = bisect_right(nums, opposite / 2, left)
        for a in nums[left:right]:
            b = opposite - a
            if b in counter and a!=b:
                ret.append([num, a, b])
print(ret)