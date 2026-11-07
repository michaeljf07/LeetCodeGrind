class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """
        sum(nums) + (moves)(n - 1) = n * (min(nums) + moves)

        sum(nums) = sum of nums
        (moves)(n - 1) = sum of move increments
        min(nums) + moves = min number of moves to equate array elements
        n * (min(nums) + moves) = sum of array with lowest equal value

        Solving for moves:
        (n - 1)(moves) - (n)(moves) = n * min(nums) - sum(nums)
        moves = sum(nums) - n * min(nums)
        """

        return sum(nums) - len(nums) * min(nums)
