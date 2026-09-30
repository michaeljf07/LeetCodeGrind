class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # every power of 2 has exactly one bit that is 1
        return n > 0 and (n & (n - 1)) == 0