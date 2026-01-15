class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return [i, complement_map[complement]]

            else:
                complement_map[num] = i