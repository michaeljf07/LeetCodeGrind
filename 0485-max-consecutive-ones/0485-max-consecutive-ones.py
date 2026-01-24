class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cur_count = 0

        for i in nums:
            if i == 1:
                cur_count += 1
                max_count = cur_count if cur_count > max_count else max_count
            else:
                cur_count = 0

        return max_count