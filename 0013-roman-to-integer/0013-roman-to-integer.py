class Solution:
    def romanToInt(self, s: str) -> int:
        str_to_val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
        length = len(s)
        cur_sum = 0
        idx = 0
        while idx < length:
            char = s[idx]
            if idx < length - 1:
                next = s[idx + 1]
                if char == 'I' and (next == 'V' or next == 'X'):
                    cur_sum += str_to_val[next] - str_to_val[char]
                    idx += 2
                elif char == 'X' and (next == 'L' or next == 'C'):
                    cur_sum += str_to_val[next] - str_to_val[char]
                    idx += 2
                elif char == 'C' and (next == 'D' or next == 'M'):
                    cur_sum += str_to_val[next] - str_to_val[char]
                    idx += 2
                else:
                    cur_sum += str_to_val[char]
                    idx += 1
            else:
                cur_sum += str_to_val[char]
                idx += 1

        return cur_sum