class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # k may be > num
        # since there are fixed number of positions, rotating beyond len(nums)
        # returns the array to the same state as if we rotated k % len(nums) times
        k = k % len(nums)

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # reverse entire list
        reverse(0, len(nums) - 1)
        # reverse elements that *were* at the end of nums
        reverse(0, k - 1)
        # reverse elements that have been shifted forwards
        reverse(k, len(nums) - 1)
