# map이나 failter 보다는 list comprehension을 사용하자.

a = [n*2 for n in range(1, 10 + 1) if n%2 == 1]

print(a)

original = {"first": 1, "second": 2, "third": 3}
b = {key: value*2 for key, value in original.items()}

print(b)