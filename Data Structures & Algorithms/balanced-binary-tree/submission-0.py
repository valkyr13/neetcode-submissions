# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def height(root: TreeNode) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            
            left = 0
            right = 0

            if root.left is not None:
                left = height(root.left)

            if root.right is not None:
                right = height(root.right)

            if abs(left-right) > 1:
                self.balanced = False
            
            return max(left+1, right+1)

        height(root)

        return self.balanced
        

        

        