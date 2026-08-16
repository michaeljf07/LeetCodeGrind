class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        
        dp = {} # (i, j) -> whether s1[i:] and s2[j:] can form s3[i + j:]
        def dfs(i: int, j: int, k: int) -> bool:
            if k == len_s3:
                return i == len_s1 and j == len_s2
            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            if i < len_s1 and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if not res and j < len_s2 and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0, 0)