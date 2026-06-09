# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float("-infinity"), float("infinity"))

    def validate(self, node: TreeNode, min_val: int, max_val: int) -> bool:
        if not node:
            return True
        
        if node.val >= max_val or node.val <= min_val:
            return False

        return (
            self.validate(node.left, min_val, node.val) and
            self.validate(node.right, node.val, max_val)
        )