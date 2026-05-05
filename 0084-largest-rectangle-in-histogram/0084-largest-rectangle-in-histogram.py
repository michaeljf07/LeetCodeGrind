class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack: tuple[int, int] = []

        for i, height in enumerate(heights):
            start = i
            while len(stack) != 0 and stack[-1][1] > height:
                pop_idx, pop_height = stack.pop()
                max_area = max(max_area, pop_height * (i - pop_idx))
                start = pop_idx
            stack.append((start, height))
            
        for i, height in stack:
            max_area = max(max_area, height * (len(heights) - i))

        return max_area