class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_and_stripped = [item.strip() for item in s.split()]
        split_and_stripped.reverse()

        for each in split_and_stripped:
            if each != "":
                return len(each)
        return 0