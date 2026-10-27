# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, current_number: int) -> int:
            if not node:
                return 0
            
            current_number = current_number * 10 + node.val
            
            if not node.left and not node.right:
                return current_number
            
            return dfs(node.left, current_number) + dfs(node.right, current_number)
            
        return dfs(root, 0)
