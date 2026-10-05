class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = []
        total_numbers = 1 << n

        for i in range(total_numbers):
            res.append(i ^ (i >> 1))

        return res