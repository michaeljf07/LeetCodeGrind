class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, char in enumerate(s):
            if char in seen:
                seen[char] = -1
            else:
                seen[char] = i
        
        for val in seen.values():
            if val != -1:
                return val

        return -1