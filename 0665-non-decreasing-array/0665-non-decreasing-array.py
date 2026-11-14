class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        changes_needed = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                changes_needed += 1
                if changes_needed > 1:
                    return False

                # nums[i - 1] <= nums[i + 1] => we can lower nums[i] to keep the
                # array in non-decreasing order (easier for array to stay non-decreasing)
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                # otherwise, we raise the next element
                else:
                    nums[i + 1] = nums[i]

        return True