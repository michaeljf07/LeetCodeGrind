class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Let A, B, and C be days s.t. A is before B, B before C.

        if A < B < C
        - profit = (B - A) + (C - B) = C - A

        else (i.e. non-contuous increasing prices)
        - we skip days until there is an increase in consecutive days
        """
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        return total_profit
