# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(root: TreeNode) -> int:
            if root is None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            m = max(left,right)
            self.res = max(self.res, m, left +right)
            return m+1

        helper(root)
        return self.res