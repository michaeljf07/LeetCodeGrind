class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            ith_bit = (n >> i) & 1 # get the ith bit
            # place the ith bit at the (31 - i)th position i.e. reverse
            res += ith_bit << (31 - i)
        return res