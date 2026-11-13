class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1

        return candidate