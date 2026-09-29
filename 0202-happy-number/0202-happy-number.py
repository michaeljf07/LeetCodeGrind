class Solution:
    def isHappy(self, n: int) -> bool:
        # Treat cycle detection like a linked list
        slow, fast = n, self.squareAndSumDigits(n)
        # reaching 1 is a cycle, but the sum of its digits always remains 1
        while slow != fast:
            fast = self.squareAndSumDigits(fast)
            fast = self.squareAndSumDigits(fast)
            slow = self.squareAndSumDigits(slow)
        return True if fast == 1 else False

    @staticmethod
    def squareAndSumDigits(n: int):
        curr_sum = 0
        while n > 0:
            digit = n % 10
            curr_sum += digit ** 2
            n = n // 10
        return curr_sum