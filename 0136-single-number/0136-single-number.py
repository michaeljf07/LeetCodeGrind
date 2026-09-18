class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # XOR is commutative and associative so it doesn't matter if we XOR adjacent numbers that are not equal
            res = res ^ num
        return res 