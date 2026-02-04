class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(len(list(filter(lambda x : x < num, nums))))
        
        return ans