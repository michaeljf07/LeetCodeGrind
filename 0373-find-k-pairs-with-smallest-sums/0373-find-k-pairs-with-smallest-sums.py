class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        min_heap = [] # (sum, index in nums1, index in nums2)
        
        """
           1 7 11        
        2 [3,9,13]
        4 [5,11,15]
        6 [7,13,17]
        
        We see that (0,0) will always be the smallest sum because nums1 and nums2 are
        sorted in non-decreasing order.
        """
        # since (0,0) is always smallest, we can push the entire first row into the heap
        # because we know that the next smallest sum is at (i+1,j) or (i,j+1). exploring this
        # way ensures that we traverse in a negative diagonal direction
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        res = []
        while min_heap and k > 0:
            _, index1, index2 = heapq.heappop(min_heap)
            res.append([nums1[index1], nums2[index2]])

            # for every (i,j) we look at the element at (i,j+1)
            if index2 + 1 < len(nums2):
                new_sum = nums1[index1] + nums2[index2 + 1]
                heapq.heappush(min_heap, (new_sum, index1, index2 + 1))

            k -= 1
        
        return res