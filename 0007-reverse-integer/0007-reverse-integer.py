class Solution:
    def reverse(self, x: int) -> int:
        # s = str(x)

        # if s[0] == '-':
        #     rev = '-' + s[:0:-1]
        # else:
        #     rev = s[::-1]
        
        # num = int(rev)
        
        # if -2**31 <= num <= 2**31 - 1:
        #     return num

        sign: int = -1 if x < 0 else 1

        rev = int(str(abs(x))[::-1]) * sign

        if (-2 ** 31) <= rev <= (2 ** 31 - 1):
            return rev
        
        return 0
        
        return 0
