# 시간초과

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

inputs = 'cbd'
max_palindrome = ''

inputs = list(inputs)

for index, word in enumerate(inputs):
    idx_list = list(filter(lambda x: inputs[x] == word, range(len(inputs))))

    for idx in idx_list:
        if index < idx:
            if isPalindrome(inputs[index: idx+1]) and len(max_palindrome) < len(inputs[index: idx+1]):
                max_palindrome = ''.join(inputs[index: idx+1])

if max_palindrome == '':
    max_palindrome = inputs[0]

print(max_palindrome)




# 책의 idea를 토대로 짜자.

def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

if len(s) < 2 or s == s[::-1]:
    return s

result = ''

for i in range(len(s) - 1):
    result = max(result,
                    expand(i, i+1),
                    expand(i, i+2),
                    key=len)
return result


# 딴 사람이 짠 것 최단 시간

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s == s[::-1]: return s

        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l - 1:r], s[l:r]

            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1

        return s[start:start + size]





