class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        write = head
        read = head.next
        temp_sum = 0
        
        while read:
            if read.val == 0:
                write.val = temp_sum
                temp_sum = 0
                if read.next:
                    write = write.next
            else:
                temp_sum += read.val
            
            read = read.next
        
        write.next = None
        return head