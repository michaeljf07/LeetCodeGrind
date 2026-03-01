class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        summ = sum(nums)
        ans = [0] * len(nums)

        for i in range(len(nums)):
            summ -= nums[i]
            ans[i] = abs(left - summ)
            left += nums[i]
        
        return ans