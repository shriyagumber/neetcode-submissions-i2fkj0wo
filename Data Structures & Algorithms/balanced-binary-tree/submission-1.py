# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        self.dfs(root)
        return self.flag

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if not self.flag: return 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        if abs(l-r) > 1:
            self.flag = False

        return 1 + max(l, r)
        