class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_last_idx = m - 1
        n_last_idx = n - 1
        right_idx = m + n - 1

        while n_last_idx >= 0:
            if m_last_idx >= 0 and nums1[m_last_idx] > nums2[n_last_idx]:
                nums1[right_idx] = nums1[m_last_idx]
                m_last_idx -= 1
            else:
                nums1[right_idx] = nums2[n_last_idx]
                n_last_idx -= 1

            right_idx -= 1
