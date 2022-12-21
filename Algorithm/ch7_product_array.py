# 나눗셈을 하지 않고 O(n)에 풀이하라.
# 나눗셈해도 되면 전체 곱만 구해서 자기 자신 나눠주면 끝

nums = [-1, 1, 0, -3, 3]
l = len(nums)

out = [1]     # 이 부분을 미리 [1]*l로 만들어놓고 밑에서 append 대신 대입으로 해도 속도는 별 차이 없다.
right = nums[l-1]

for i in range(1, l):
    out.append(out[i-1]*nums[i-1])


for j in range(1, l):
    out[l-1-j] = right * out[l-1-j]
    right = right * nums[l-1-j]

print(out)