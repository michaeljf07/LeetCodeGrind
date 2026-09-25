class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)

        res = 0 

        while x > 0:
            # shift digits to right by one and add last number in x
            res = (res * 10) + (x % 10)
            x //= 10
        
        if res > 2**31 - 1:
            return 0

        return res * -1 if is_negative else res