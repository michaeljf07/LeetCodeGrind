class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first: bool) -> int:
            """Find the first or last index of target in nums"""
            left = 0
            right = len(nums) - 1

            bound = -1 # default for when target not in nums
            # [5, 7, 7, 9, 9, 9, 10]

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if is_first:
                        # first posn must be to the left of mid
                        right = mid - 1
                    else:
                        # last posn must be to the right of mid
                        left = mid + 1
                    bound = mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return bound
             
        return [find_bound(True), find_bound(False)]