# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_seen = float("-infinity")

        def dfs(node: TreeNode):
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)
            
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            current_path_sum = node.val + left_max + right_max

            self.max_seen = max(self.max_seen, current_path_sum)

            return node.val + max(left_max, right_max)

        dfs(root)

        return self.max_seen