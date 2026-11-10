class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INVALID_DEFAULT = float("inf")

        dp = [INVALID_DEFAULT] * (amount + 1) # dp[amount] = fewest number of coins to make amount
        dp[0] = 0

        for coin in coins:
            for amount in range(coin, amount + 1):
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

        return dp[amount] if dp[amount] != INVALID_DEFAULT else -1