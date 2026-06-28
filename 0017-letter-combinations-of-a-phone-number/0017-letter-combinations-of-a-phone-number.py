class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i: int, cur: str):
            if len(cur) == len(digits):
                res.append(cur)
                return

            for char in digit_to_char[digits[i]]:
                backtrack(i + 1, cur + char)

        if digits:
            backtrack(0, "")

        return res