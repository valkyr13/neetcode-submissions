# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]):

        if root == None:
            return float('-inf'), 0


        l, l_down = self.helper(root.left)

        r, r_down = self.helper(root.right)

        curr_path = l_down+r_down+root.val

        max_down = max(l_down+root.val, r_down+root.val,root.val)

        maxSum = max(max_down, curr_path, l,r)

        return (maxSum, max_down)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        do we consider max of negative sums
        should -inf, or zero?
        """
        maxSum, _ =  self.helper(root)
        return maxSum



