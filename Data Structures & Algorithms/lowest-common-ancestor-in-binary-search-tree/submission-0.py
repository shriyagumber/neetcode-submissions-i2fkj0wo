# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root,p,q)

    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root.val == p.val or root.val == q.val:
            return root
        
        l = self.dfs(root.left, p, q)
        r = self.dfs(root.right, p, q)

        if l is None and r is None: return None
        elif l is None and r is not None: return r
        elif l is not None and r is None: return l
        else: return root