T = [73, 74, 75, 71, 69, 72, 76, 73]


answer = [0] * len(T)
stack = []

for i, cur in enumerate(T):
    while stack and cur > T[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last

    stack.append(i)

print(answer)
