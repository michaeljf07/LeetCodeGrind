class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first: dict = {}  # tracks first occurence of a number
        last: dict = {}   # tracks last occurence of a number
        count: dict = {}  # tracks the number of times each number appears
        
        for i, num in enumerate(nums):
            if num not in first: 
                first[num] = i

            last[num] = i
            count[num] = count.get(num, 0) + 1
            
        degree: int = max(count.values())
        
        # Find the minimum length among numbers that hit the degree
        min_len: int = len(nums)
        for x in count:
            if count[x] == degree:
                min_len = min(min_len, last[x] - first[x] + 1)
                
        return min_len