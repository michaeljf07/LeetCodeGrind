# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy_less = ListNode(0, None)  # carries nodes < x
        dummy_ge = ListNode(0, head)    # tracks the head of nodes >= x

        curr = head
        last_attached = dummy_ge
        detached = dummy_less
        while curr:
            if curr.val < x:
                detached.next = curr
                detached = detached.next
                last_attached.next = curr.next
            else:
                last_attached = curr
            
            curr = curr.next
        
        detached.next = dummy_ge.next
        return dummy_less.next