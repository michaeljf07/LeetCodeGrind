# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self._push_all_in_left_branch(root)

    def next(self) -> int:
        next_node = self.stack.pop()
        self._push_all_in_left_branch(next_node.right)
        return next_node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0

    def _push_all_in_left_branch(self, node: TreeNode) -> None:
        while node is not None:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()