class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1) # dp[i] = the number of 1 bits in i
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp