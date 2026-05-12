class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = left + (right - left) // 2
            hours_needed = 0
            for pile in piles:
                hours_needed += pile // k if pile % k == 0 else pile // k + 1
            
            if hours_needed <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res