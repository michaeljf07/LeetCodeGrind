class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INVALID_DEFAULT = float("inf")
        dp = [INVALID_DEFAULT] * (amount + 1) # dp[a] = the fewest number of coins to make amount a
        dp[0] = 0

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - coin])
        
        return dp[amount] if dp[amount] != INVALID_DEFAULT else -1