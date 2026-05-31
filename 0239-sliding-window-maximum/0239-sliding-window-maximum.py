from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        left = right = 0

        for right in range(len(nums)):
            # remove elements prev max as they move outside the window
            left = right - k + 1
            if dq and dq[0] < left:
                dq.popleft()

            # remove elements from the end which can never be max again
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            if right >= k - 1:
                res.append(nums[dq[0]])

        return res