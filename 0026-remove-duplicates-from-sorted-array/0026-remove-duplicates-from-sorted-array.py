class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nxt_unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[nxt_unique] = nums[i]
                nxt_unique += 1
                
        return nxt_unique