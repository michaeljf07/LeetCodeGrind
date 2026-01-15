class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        if any(s == "" for s in strs):
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = ""
        min_length = min(len(s) for s in strs)
        
        for i in range(min_length):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return prefix
            prefix += current_char
        
        return prefix