# 너무나도 오래걸린다. 돌아가긴하지만..
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
nums.sort()
result_lst = []

for i in range(len(nums)):
    left = i+1
    right = len(nums)-1

    while left < right and nums[i] <= 0:
        if (i != 0 and nums[i] != nums[i-1]) or i == 0:
            if nums[left] + nums[right] + nums[i] < 0:
                left += 1
            elif nums[left] + nums[right] + nums[i] > 0:
                right -= 1
            else:
                if left > i+1 and right < len(nums) - 1:
                    if nums[left] != nums[left-1]:
                        result_lst.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    else:
                        left += 1
                        right -= 1
                else:
                    result_lst.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        else:
            break

print(result_lst)


# 최고 내거보다 6배~최대 10배 가까이 빠름

import collections
from bisect import bisect_right, bisect_left

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
return ret