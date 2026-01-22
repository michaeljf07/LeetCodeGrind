class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = {}

        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1
        
        for char in t:
            if char not in s:
                return char
            elif t.count(char) > s_count[char]:
                return char

        return ""