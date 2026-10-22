"""
Input: array of ints in non-decreasing order

- edit array in place
- each element appears at most twice
- relative order kept same
- does not matter what is left after k elements

Constrains:
- O(1) space
- 1 <= nums.length <= 3 * 104

0,0,1,1,1,1,2,3,3
^
out
^
in
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        out = 2
        for in_idx in range(2, n):
            # check if the current number does not appears twice already
            if nums[in_idx] != nums[out - 2]:
                nums[out] = nums[in_idx]
                out += 1

        return out