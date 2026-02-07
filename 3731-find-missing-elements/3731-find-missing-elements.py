class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(min(nums) + 1, max(nums)):
            if i not in nums:
                ans.append(i)

        return ans