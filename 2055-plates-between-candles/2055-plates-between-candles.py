class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        prefix_plates = [0] * (n + 1)  # total number of plates before index i
        left_candle = [-1] * n  # index of the nearest candle at or to the left of i
        right_candle = [-1] * n  # index of the nearest candle to the right of i

        last_candle = -1
        for i in range(n):
            prefix_plates[i + 1] = prefix_plates[i] + (1 if s[i] == "*" else 0)
            if s[i] == "|":
                last_candle = i
            left_candle[i] = last_candle

        next_candle = -1
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                next_candle = i
            right_candle[i] = next_candle

        answer = []
        for left, right in queries:
            l = right_candle[left]
            r = left_candle[right]
            if l != -1 and r != -1 and l < r:
                answer.append(prefix_plates[r] - prefix_plates[l])
            else:
                answer.append(0)

        return answer
