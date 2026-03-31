# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None: return True
        if root is None: return False

        return self.find(root, subRoot)

    def find(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: return False

        l = self.find(root.left, subRoot)

        if root.val == subRoot.val:
            if self.isSame(root, subRoot): return True

        r = self.find(root.right, subRoot)

        return l or r


    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None and q is not None: return False
        if p is not None and q is None: return False
        if p.val != q.val: return False

        l = self.isSame(p.left, q.left)
        r = self.isSame(p.right, q.right)

        return l and r