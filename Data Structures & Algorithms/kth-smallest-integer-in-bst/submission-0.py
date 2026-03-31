# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       self.flag = True
       self.val = -1
       self.count = 0
       self.dfs(root, k)

       return self.val
    
    def dfs(self, root: Optional[TreeNode], k: int) -> None:
        if root is None: return
        if not self.flag: return

        self.dfs(root.left, k)

        self.count += 1
        if self.count == k: 
            self.flag = False
            self.val = root.val

        self.dfs(root.right, k)
        

        