# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        re = []
        q = []
        q.append(root)

        while q:
            sz = len(q)
            li = []

            for i in range(sz):
                curr = q.pop(0)
                li.append(curr.val)

                if curr.left is not None: q.append(curr.left)
                if curr.right is not None: q.append(curr.right)
            

            re.append(li)
        
        return re