class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        dp = [-1] * n  # dp[i] = max amount of money we can rob in the first i houses
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            skip = dp[i - 1]
            rob = nums[i] + dp[i - 2]
            dp[i] = max(skip, rob)

        return dp[-1]
