# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        dummy = ListNode(-1)
        temp = dummy


        for list in lists:
            if list is not None:
                heapq.heappush(pq, (list.val, id(list), list))
        

        while pq:
            _, _, curr = heapq.heappop(pq)
            temp.next = curr
            temp = temp.next
            if curr.next is not None:
                heapq.heappush(pq, (curr.next.val, id(curr.next), curr.next))
        

        return dummy.next