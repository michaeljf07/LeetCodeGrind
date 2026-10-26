class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        cur_sum = 0
        min_len = float("inf")

        for right in range(len(nums)):
            cur_sum += nums[right]

            # Shrink window from the left as long as the sum is >= target
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len