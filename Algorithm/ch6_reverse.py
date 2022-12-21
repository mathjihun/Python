# Question: How can reverse the given sequence?

# Mine 274ms, 18.4MB

class Solution:
    def reverseString(self, s: List[str]) -> None:
       for i in range(len(s)//2):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]



# Answer 1 268ms, 18.4MB

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# Answer 2 253ms, 18.5MB
# 1보다 조금 빠르다.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()