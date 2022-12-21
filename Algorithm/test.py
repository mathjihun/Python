def isPalindrome(s):
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    for idx in range(len(strs) // 2):
        if strs[idx] != strs[len(strs) - idx - 1]:
            return False
    else:
        return True

inputs = 'babad'
max_palindrome = ''

inputs = list(inputs)

for idx, word in enumerate(inputs):



if max_palindrome == '':
    max_palindrome = inputs[0]

print(max_palindrome)