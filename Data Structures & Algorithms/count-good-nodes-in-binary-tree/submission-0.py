# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def helper(root:TreeNode, val: int):
            if root is None:
                return 
            
            if root.val >= val:
                self.count += 1
                val = max(val,root.val)
            helper(root.left,val)
            helper(root.right,val)
        
        helper(root,-101)
        return self.count
        