# 내가 한 것

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums).most_common()
        lst = []

        for x in d:
            if len(lst) < k:
                lst.append(x[0])

        return lst

# 교재 코드 길이를 더 줄일 수 있다.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]