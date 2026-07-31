"""
- path: str - represents the file path in a unix system
  - must start with a /
  - directories must be separated by a /
  - . = current
  - .. = previous

path = "/home/user/Documents/./Pictures"
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)

        final_path = '/' + '/'.join(stack)
        return final_path