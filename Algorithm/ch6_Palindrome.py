# Ouestion: Is the given sentence a palindrome?
# LeetCode

# Mine 67ms, 19.2MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        for idx in range(len(strs)//2):
            if strs[idx] != strs[len(strs)-idx-1]:
                return False
        else:
            return True


# Answer 1 273 ms, 19.3MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


# Answer 2 91ms, 19.2MB
# Use deque (faster than Answer 1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


# Answer 3 54ms, 15.6MB
# C로 구현되어 있어서 Answer 2보다도 더 빠르다.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]