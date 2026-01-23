class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if not isinstance(num, int):
            return False
        else:
            possible_range: list = range(1, num + 1)
            left: int = possible_range[0]
            right: int = possible_range[-1]

            while left <= right:
                mid = (left + right) // 2
                mid_sqr = mid ** 2

                if mid_sqr == num:
                    return True
                elif mid_sqr > num:
                    right = mid - 1 
                else:
                    left = mid + 1

            return False