class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] = whether s[i:] can be segmented
        dp[len(s)] = True # Base Case

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                """
                Conditions to be able to compare:
                - The index and the length of the word cannot overshoot s
                - The segment we are looking at matches word 
                """
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]
