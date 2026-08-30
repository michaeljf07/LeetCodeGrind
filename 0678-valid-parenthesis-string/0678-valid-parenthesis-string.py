class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0 # the min number of '(' that could be open
        left_max = 0 # the max number of '(' that could be open

        for char in s:
            if char == '(':
                left_min += 1
                left_max += 1
            elif char == ')':
                left_min -= 1
                left_max -= 1
            elif char == '*':
                left_min -= 1
                left_max += 1

            # Too many closing parentheses
            if left_max < 0:
                return False
            # Encountered extra '*' => treat as ""           
            if left_min < 0:
                left_min = 0
        
        return left_min == 0