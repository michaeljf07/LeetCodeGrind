class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = {}

        for char in s:
            if char not in s_counter:
                s_counter[char] = 1
            else:
                s_counter[char] += 1

        for char in t:
            if char not in s_counter or s_counter[char] == 0:
                return False
            else:
                s_counter[char] -= 1

        return True