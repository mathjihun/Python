import collections

s = "bcabc"

counter, stack = collections.Counter(s), collections.deque()

for char in s:
    counter[char] -= 1

    if char in stack:
        continue

    while stack and char < stack[-1] and counter[stack[-1]] > 0:
        stack.pop()
    stack.append(char)

print(''.join(stack))