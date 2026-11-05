class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # must at a peak or peak is to the left of mid
            if nums[mid] > nums[mid + 1]:
                right = mid
            # peak is to the right of mid
            else:
                left = mid + 1

        # left == right, pointing to a peak element
        return left