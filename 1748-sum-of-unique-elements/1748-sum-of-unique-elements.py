class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        ans_sum = 0
        for key, val in counter.items():
            if val == 1:
                ans_sum += key

        return ans_sum