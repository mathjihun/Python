# 내 풀이 O(n^2)

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

max_index = height.index(max(height))
idx = 0
sums = 0
total_sums = 0

while idx < max_index:
    for k in range(idx+1, max_index+1):
        if height[idx] > height[k]:
            sums += height[k]
        else:
            total_sums += height[idx]*(k-idx-1) - sums
            idx = k
            sums = 0
            break


idx = len(height) - 1

while idx > max_index:
    for k in range(idx-1, max_index-1, -1):
        if height[idx] > height[k]:
            sums += height[k]
        else:
            total_sums += height[idx]*(idx-k-1) - sums
            idx = k
            sums = 0
            break

print(total_sums)


# 다른 풀이

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height_len = len(height)

max_index = height.index(max(height))
idx = 0
sums = 0

while idx < max_index:
    if height[idx] >= height[idx+1]:
        sums += height[idx] - height[idx+1]
        height[idx+1] = height[idx]
    idx += 1

idx = height_len - 1

while idx > max_index:
    if height[idx] >= height[idx-1]:
        sums += height[idx] - height[idx-1]
        height[idx-1] = height[idx]
    idx -= 1

print(sums)

# 1위인 코드 그런데 내가 돌리면 성능이 안 나옴

l = 0
r = len(height) - 1
ans = 0
lmax = 0
rmax = 0
while l < r:
    if height[l] < height[r]:
        if height[l] >= lmax:
            lmax = height[l]
        else:
            ans += lmax - height[l]
        l += 1
    else:
        if height[r] >= rmax:
            rmax = height[r]
        else:
            ans += rmax - height[r]
        r -= 1

print(ans)