"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return head

        dummy = Node(head.val)
        temp = dummy

        map = {}
        map[None] = None
        map[head] = temp

        while head:
            if head.next in map:
                temp.next = map[head.next]
            else:
                map[head.next] = Node(head.next.val)
                temp.next = map[head.next]
            
            if head.random in map:
                temp.random = map[head.random]
            else:
                map[head.random] = Node(head.random.val)
                temp.random = map[head.random]
            
            temp = temp.next
            head = head.next
        
        return dummy
                


        