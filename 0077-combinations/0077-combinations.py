class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        path = []
        def backtrack(i: int, path: list[int]):
            if len(path) >= k:
                res.append(path.copy())
                return

            if i > n:
                return

            path.append(i)
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)

        backtrack(1, path)
        return res