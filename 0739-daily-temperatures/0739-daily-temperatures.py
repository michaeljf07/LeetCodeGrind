class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack: tuple[int, int] = []

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx

            stack.append((temp, i))

        return res