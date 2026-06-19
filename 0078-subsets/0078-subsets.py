class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            copy = list(res)
            for subset in copy:
                res.append(subset + [num])

        return res