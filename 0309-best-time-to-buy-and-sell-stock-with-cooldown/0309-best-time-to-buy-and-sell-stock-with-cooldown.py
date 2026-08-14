class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        held = -float('inf')  # Cannot hold stock before day 0 without buying
        sold = 0
        rest = 0

        for price in prices:
            prev_sold = sold
            
            sold = held + price
            held = max(held, rest - price)
            rest = max(rest, prev_sold)

        return max(sold, rest) 