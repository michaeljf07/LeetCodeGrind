class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        for char in t:
            if char in counter:
                counter[char] -= 1
                if counter[char] < 0:
                    return False
            else:
                return False

        for key in counter:
            if counter[key] != 0:
                return False

        return True