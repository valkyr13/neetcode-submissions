# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def helper(self, preorder: List[int], a: int, b: int, inorder:List[int], c: int, d:int) -> Optional[TreeNode]:
        if a > b or c > d:
            return None
        root = TreeNode(preorder[a])
        idx = inorder.index(preorder[a])
        l = idx-c
        root.left = self.helper(preorder, a+1,a+l, inorder, c, idx-1)
        root.right = self.helper(preorder, a+l+1, b, inorder, idx+1, d)
        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        1. root, l, r
        2. l, root, r
        identify root in 2 - x
        0, x-1 - l
        x+1, n - r
        """
        n = len(preorder)
        return self.helper(preorder,0,n-1,inorder, 0, n-1)

        