# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        idx = 0
        node_map = {} # idx: node
        while curr:
            node_map[idx] = curr
            curr = curr.next
            idx += 1

        rem_idx = idx - n

        if rem_idx == 0:
            return head.next

        prev_node = node_map[rem_idx - 1]
        prev_node.next = node_map[rem_idx].next

        return head