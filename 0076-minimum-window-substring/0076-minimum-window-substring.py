class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        count_t = {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        window = {}
        have = 0 # num of distinct chars in the window
        need = len(count_t)

        res = [-1, -1]
        res_len = float("infinity")

        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # shrink window
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        left, right = res

        return s[left : right + 1] if res_len != float("infinity") else ""

