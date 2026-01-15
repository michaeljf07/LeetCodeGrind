class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]" and len(stack) > 0:
                if bracket_map[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False