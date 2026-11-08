class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # for s to be a subsequence of t, we must have len(s) <= len(t)
        if len(s) > len(t):
            return False

        s_ptr = 0
        t_ptr = 0
        
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1
            
        # If s_ptr reached the end, all characters were found in order
        return s_ptr == len(s)
