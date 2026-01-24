class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = str(bin(x)[2:].zfill(32))
        y = str(bin(y)[2:].zfill(32))
        ans = 0
        for i in range(32):
            if x[i] != y[i]:
                ans += 1
        return ans
