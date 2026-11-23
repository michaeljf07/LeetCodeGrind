class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        PLATE, CANDLE = '*', '|'
        answer = []
        n = len(s)

        # left_candles[i] = nearest candle index at or to the left of i
        left_candles = [-1] * n
        # right_candles[i] = nearest candle index at or to the right of i
        right_candles = [-1] * n
        # total_plates[i] = total number of plates strictly before index i
        total_plates = [0] * (n + 1)

        closest_left_candle = -1
        for i in range(n):
            total_plates[i + 1] = total_plates[i] + (1 if s[i] == PLATE else 0)
            if s[i] == CANDLE:
                closest_left_candle = i
            left_candles[i] = closest_left_candle

        closest_right_candle = -1
        for i in range(n - 1, -1, -1):
            if s[i] == CANDLE:
                closest_right_candle = i
            right_candles[i] = closest_right_candle

        for left, right in queries:
            l = right_candles[left]
            r = left_candles[right]
            if l != -1 and r != -1 and l < r:
                answer.append(total_plates[r + 1] - total_plates[l])
            else:
                answer.append(0)

        return answer