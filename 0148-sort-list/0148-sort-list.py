# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next

        nodes.sort()
        dummy = ListNode(0, None)
        cur = dummy
        
        for val in nodes:
            cur.next = ListNode(val, None)
            cur = cur.next

        return dummy.next
