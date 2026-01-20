class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        end = len(nums) - 1

        while i <= end:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            
            i += 1
