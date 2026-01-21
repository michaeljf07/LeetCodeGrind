class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        search_bounds = range(1, x // 2 + 1)

        for n in search_bounds:
            if n * n == x:
                return n
            elif not (n+1) * (n+1) <= x:
                return n
            