# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while carry or l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            digit_sum = l1_val + l2_val + carry
            carry = digit_sum // 10

            new_node = ListNode(digit_sum % 10)
            cur.next = new_node
            cur = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        