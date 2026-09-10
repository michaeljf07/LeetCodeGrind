class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}  # (pos_s, pos_t) -> number of ways to form t[pos_t:] from s[pos_t]

        def dfs(pos_s: int, pos_t: int) -> int:
            # valid subsequence formed
            if pos_t == len(t):
                return 1
            # reached end of s before fully matching t
            if pos_s == len(s):
                return 0

            if (pos_s, pos_t) in memo:
                return memo[(pos_s, pos_t)]

            res = dfs(pos_s + 1, pos_t)  # always consider skipping the current letter
            # if the letters in s and t match, we consider using this character and move the the next chars
            if s[pos_s] == t[pos_t]:
                res += dfs(pos_s + 1, pos_t + 1)

            memo[(pos_s, pos_t)] = res
            return res

        return dfs(0, 0)
