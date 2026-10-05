class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                # multiply the two single digits and add to previous carry/value
                mul = d1 * d2 + res[i + j + 1]
                # update the current position and carry over to the next
                res[i + j + 1] = mul % 10
                res[i + j] += mul // 10

        # skip leading zero if present
        start_idx = 0
        while start_idx < len(res) and res[start_idx] == 0:
            start_idx += 1

        return "".join(chr(d + ord('0')) for d in res[start_idx:])

