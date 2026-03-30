# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        self.maxSum = float("-inf")
        self.dfs(root)
        return self.maxSum
    
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        l = max(0, self.dfs(root.left))
        r = max(0, self.dfs(root.right))

        self.maxSum = max(self.maxSum, root.val + l + r)

        return root.val + max(l, r)
        