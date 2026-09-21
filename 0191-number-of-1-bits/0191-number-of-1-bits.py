class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # n & 1 checks if the last bit is 1
            res += 1 if n & 1 else 0
            n >>= 1
        return res
