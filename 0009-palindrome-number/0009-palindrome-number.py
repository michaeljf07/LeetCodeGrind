class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev = 0
            x_copy = x

            while x > 0:
                rev = (rev * 10) + (x % 10)
                x = x // 10
            
            return rev == x_copy
