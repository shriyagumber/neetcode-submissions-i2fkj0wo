# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, inorder)
    

    def build(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        rootVal = preorder[0]
        root = TreeNode(rootVal)

        for i in range(len(inorder)):
            if inorder[i] == rootVal:
                inorder_left = inorder[:i]
                inorder_right = inorder[i+1:]

        preorder_left = preorder[1 : len(inorder_left) + 1]
        preorder_right = preorder[len(inorder_left) + 1 :]

        root.left = self.build(preorder_left, inorder_left)
        root.right = self.build(preorder_right, inorder_right)


        return root