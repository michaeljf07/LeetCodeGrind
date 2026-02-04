class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        temp = []

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            sub_array = nums[start:i+1]
            temp.append(sum(sub_array))

        return sum(temp)