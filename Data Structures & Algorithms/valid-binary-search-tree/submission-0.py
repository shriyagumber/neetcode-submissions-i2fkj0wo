# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.prev = None
        self.dfs(root)
        return self.ans

    def dfs(self, root: Optional[TreeNode]) -> None:
        if root is None: return
        
        self.dfs(root.left)

        if self.prev is not None and self.prev.val >= root.val:
            self.ans = False
        self.prev = root

        self.dfs(root.right)

        