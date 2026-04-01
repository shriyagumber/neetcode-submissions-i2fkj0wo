# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy

        def reverse(before, after):

            prev = after
            curr = before.next

            while curr != after:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            before.next = prev

        
        while True:

            before = temp

            for i in range(k):
                if temp is None: break
                temp = temp.next

            if temp is None: break

            after = temp.next
            tail = before.next

            reverse(before, after)

            temp = tail
        
        return dummy.next
        