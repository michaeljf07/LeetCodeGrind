class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ptr = 0

        for num in nums:
            if num % 2 == 0:
                nums[ptr] = 0
                ptr += 1
        
        for i in range(ptr, n):
            nums[i] = 1

        return nums