# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:

    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root: Optional[TreeNode]):
            if root is None:
                res.append("null")
                return
            
            dfs(root.left)
            dfs(root.right) 
            res.append(str(root.val))

            return
        # postorder === dfs
        ## post order is reverse of preorder
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        self.i  = len(res)-1

        def dfs():
            if res[self.i] == "null":
                self.i -= 1
                return None
            
            node = TreeNode(int(res[self.i]))
            self.i -= 1
            node.right = dfs()            
            node.left = dfs()


            return node


        return dfs()
