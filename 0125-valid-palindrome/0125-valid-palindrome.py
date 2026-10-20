class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            if not self.isAlphaNumeric(s[left]):
                left += 1
                continue
            if not self.isAlphaNumeric(s[right]):
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True

    def isAlphaNumeric(self, char: str) -> bool:
        return (
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )