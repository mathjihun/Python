# 내가 푼 첫 풀이 느리다.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        length = 1

        for i in range(len(s)):
            while length < len(s) - i and len(set(s[i:i + length + 1])) > length:
                length += 1
                start = i

        return len(s[start:start + length])


# 책 풀이


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)

            used[char] = idx

        return max_length

