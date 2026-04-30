class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        num_zeros = 0
        for num in nums:
            if num == 0:
                num_zeros += 1
            else:
                total_product *= num

        if num_zeros >= 2:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if num_zeros == 1:
                if nums[i] == 0:
                    res[i] = total_product
            else:
                res[i] = total_product // num

        return res