class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{' }
        for each in s:
            if each in ['(', '[', '{']:
                stack.append(each)
                continue
            
            if len(stack) == 0:
                return False

            popped = stack.pop()
            if closeToOpen[each] != popped:
                return False

        if len(stack) != 0:
            return False
        else:
            return True