class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}  # (pos_s, pos_p) -> whether s[pos_s:] matches pattern p[pos_p:]

        def dfs(pos_s: int, pos_p: int) -> bool:
            # Pattern exhausted: valid match only if string is also exhausted
            if pos_p == len(p):
                return pos_s == len(s)

            if (pos_s, pos_p) in memo:
                return memo[(pos_s, pos_p)]

            cur_char_match: bool = pos_s < len(s) and (s[pos_s] == p[pos_p] or p[pos_p] == ".")

            # Next char is wildcard '*'; we can repeat pattern char p[pos_p] 0 or more times
            if (pos_p + 1) < len(p) and p[pos_p + 1] == '*':
                res = (
                    dfs(pos_s, pos_p + 2) # use p[pos_p] 0 times (skip)
                    or (cur_char_match and dfs(pos_s + 1, pos_p)) # use p[pos_p] 1+ times
                )
            elif cur_char_match:
                res = dfs(pos_s + 1, pos_p + 1) # characters match, advance both pointers
            else:
                res = False
            
            memo[(pos_s, pos_p)] = res
            return res

        return dfs(0, 0)
            