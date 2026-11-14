class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        max_sum = cur_max_sum = nums[0]
        min_sum = cur_min_sum = nums[0]
        total_sum = nums[0]

        for i in range(1, len(nums)):
            cur_max_sum = max(nums[i], cur_max_sum + nums[i])
            max_sum = max(max_sum, cur_max_sum)

            cur_min_sum = min(nums[i], cur_min_sum + nums[i])
            min_sum = min(min_sum, cur_min_sum)
            
            total_sum += nums[i]

        # the max subarray sum is the total sum of the array - the min subarray sum
        circular_sum = total_sum - min_sum

        # if all numbers are negative, the max_sum < 0 and the circular sum == 0.
        # we need to return the max negative value
        if circular_sum == 0:
            return max_sum

        return max(max_sum, circular_sum)
