class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negated = [-num for num in nums]
        heapq.heapify(negated)

        for _ in range(k - 1):
            heapq.heappop(negated)

        return -negated[0]