class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum == 0:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicate numbers from the left
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1

        return res