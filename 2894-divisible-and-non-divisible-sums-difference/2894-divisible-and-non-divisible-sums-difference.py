class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums = range(1, n + 1)

        num1 = sum([i for i in nums if i % m != 0])
        num2 = sum([i for i in nums if i % m == 0])

        return num1 - num2