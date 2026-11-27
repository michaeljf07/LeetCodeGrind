class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        num_target = 0
        num_smaller_than_target = 0
        
        for num in nums:
            if num == target:
                num_target += 1
            elif num < target:
                num_smaller_than_target += 1
                
        return list(range(num_smaller_than_target, num_smaller_than_target + num_target))