# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]):
        if root is None:
            return float('-inf'), float('-inf')

        lmax = 0
        l = 0
        rmax = 0
        r = 0
        lmax, l = self.helper(root.left)
        rmax, r = self.helper(root.right)

        localmax = max(l+root.val, r+root.val, root.val)

        gmax = max(localmax, lmax, rmax, l+root.val+r)
        
        return gmax, localmax


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        gmax, _ = self.helper(root)
        return gmax

        