import collections

nums = [1, 4, 3, 2]
nums.sort()

x = 0

for i in range(0, len(nums), 2):
    x += nums[i]

print(x)

# 한 문장으로도 구현 가능

print(sum(sorted(nums)[::2]))