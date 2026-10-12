# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        # if the list is null or the points are the same, no work is needed
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        
        before_left = dummy
        for _ in range(left - 1):
            before_left = before_left.next

        curr = before_left.next # curr is at left
        prev = None

        # there are (right - left + 1) nodes in the subsegment to reverse
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # reconnect the two ends
        before_left.next.next = curr
        before_left.next = prev

        return dummy.next