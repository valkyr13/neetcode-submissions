# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        search for p, q
        if t-l = p , t-r = q - > t
        1. p, q in l
        2. p, q in r
        3. p in l and q in r
        4. q in l and p in r

        """ 
        if (root == None):
            return root

        if (p.val == root.val or q.val == root.val):
            return root

        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p,q)

        if (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p,q)

        return root