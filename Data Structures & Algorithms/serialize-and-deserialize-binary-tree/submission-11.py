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

        if root is None:
            return "null"

        res.append(str(root.val))
        q = deque()
        q.append(root)

        while(q):
            curr = q.popleft()

            if curr.left:
                res.append(str(curr.left.val))
                q.append(curr.left)
            else:
                res.append("null")
            
            
            if curr.right:
                res.append(str(curr.right.val))
                q.append(curr.right)
            else:
                res.append("null")

        # level order === bfs
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        res = data.split(",")
        if res[0] == "null":
            return None
        q = deque()
        root = TreeNode(int(res[0]))
        q.append(root)
        i = 1
        n = len(res)

        while (q and i < n):
            curr = q.popleft()

            if i < n and res[i] != "null":
                curr.left = TreeNode(int(res[i]))
                q.append(curr.left)
            
            i += 1

            if i < n and res[i] != "null":
                curr.right = TreeNode(int(res[i]))
                q.append(curr.right)
            
            i += 1

        return root
