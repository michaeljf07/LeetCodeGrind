class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        max_freq = 0
        counts = {}

        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            max_freq = max(max_freq, counts[s[right]])

            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest