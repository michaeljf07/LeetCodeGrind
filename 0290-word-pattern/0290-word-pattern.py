class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        pattern_to_s, s_to_pattern = {}, {}

        for pattern_char, s_word in zip(pattern, s):
            if pattern_char in pattern_to_s and pattern_to_s[pattern_char] != s_word:
                return False 
            if s_word in s_to_pattern and s_to_pattern[s_word] != pattern_char:
                return False

            pattern_to_s[pattern_char] = s_word
            s_to_pattern[s_word] = pattern_char
        
        return True