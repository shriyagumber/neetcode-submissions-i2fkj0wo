# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        self.dfs(root)
        return self.ans - 1
    
    def dfs(self,  root: Optional[TreeNode]) -> int:
        if root is None: return 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        self.ans = max(self.ans, 1 + l + r)

        return 1 + max(l, r)