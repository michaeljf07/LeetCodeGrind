class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s, counter_t = {}, {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in counter_s:
                counter_s[char] = 1
            else:
                counter_s[char] += 1

        for char in t:
            if char not in counter_t:
                counter_t[char] = 1
            else:
                counter_t[char] += 1

        return counter_s == counter_t