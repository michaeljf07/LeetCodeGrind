from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        most_common = counts.most_common(k)

        res = []
        for num, count in most_common:
            res.append(num)

        return res