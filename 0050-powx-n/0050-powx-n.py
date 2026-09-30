class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        
        # we observe that there are two cases:
        # n is even => x^n = (x^2)^(n/2)
        # n is odd  => x^n = x * (x^2)^((n-1)/2)
        if n % 2 == 1:
            return x * self.myPow(x * x, n // 2)
        return self.myPow(x * x, n // 2)