# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        averages = []

        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            level_sum = 0

            for _ in range(level_size):
                cur_node = q.popleft()
                level_sum += cur_node.val
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            
            averages.append(level_sum / level_size)

        return averages
