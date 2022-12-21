# 내 풀이 O(n)이긴 하지만 너무 느리다.

prices = [7, 1, 5, 3, 6, 4]
max_benefit = 0
max_prices = 0
left = []

for i in range(len(prices)):
    if i == 0:
        left.append(prices[i])
    else:
        if prices[i] <= left[i-1]:
            left.append(prices[i])
        else:
            left.append(left[i-1])

for j in range(len(prices)-1, 0, -1):
    if j == len(prices)-1:
        max_prices = prices[j]
        max_benefit = prices[j] - left[j]
    else:
        if prices[j] >= max_prices:
            max_prices = prices[j]

        if max_benefit < (max_prices - left[j]):
            max_benefit = max_prices - left[j]

print(max_benefit)


# 책 풀이

import sys

profit = 0
min_price = sys.maxsize

for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)
