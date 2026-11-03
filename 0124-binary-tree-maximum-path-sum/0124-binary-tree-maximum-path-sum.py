# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_seen = float("-infinity")

        def dfs(root: TreeNode | None) -> None:
            if not root:
                return 0
            
            # find max path sum of left and right subtrees
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            # if path sum is negative, exclude it (set sum to 0)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # update max_seen with current path
            current_path = root.val + left_max + right_max
            self.max_seen = max(self.max_seen, current_path)

            return root.val + max(left_max, right_max)
        
        dfs(root)
        return self.max_seen