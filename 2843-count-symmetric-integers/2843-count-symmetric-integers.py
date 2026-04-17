class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            
            if n % 2 != 0:
                continue
            
            mid = n // 2
            first_half = s[:mid]
            second_half = s[mid:]
            
            sum_first = sum(int(digit) for digit in first_half)
            sum_second = sum(int(digit) for digit in second_half)
            
            if sum_first == sum_second:
                ans += 1
                
        return ans
