class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            rev = n // 2
            count += rev
            n = n - rev
            
        return count