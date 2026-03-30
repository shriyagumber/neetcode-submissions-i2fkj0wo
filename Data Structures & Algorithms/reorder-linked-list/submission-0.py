# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        firstHead = head
        secondHead = self.reverse(slow)

        while firstHead:
            temp = firstHead.next
            firstHead.next = secondHead
            firstHead = firstHead.next
            secondHead = temp


    def reverse(self, node: ListNode) -> ListNode:
        prev = None
        curr = node

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev    