class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        cur_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], cur_max = cur_max, max(cur_max, arr[i])
        return arr