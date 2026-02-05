class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0

        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                ans += 1
            elif ruleKey == "color" and ruleValue == item[1]:
                ans += 1
            elif ruleKey == "name" and ruleValue == item[2]:
                ans += 1

        return ans