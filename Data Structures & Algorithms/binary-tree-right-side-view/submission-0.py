# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        lever order traversal?
        at each level pick the last element

        """
        if not root:
            return []
        res = []
        q = deque()

        q.append((root,0))
        levelMap = defaultdict(int)
        levelMap[0] = 1


        while(len(q) != 0):
            r, lvl = q.popleft()
            if levelMap[lvl] == 1:
                res.append(r.val)
            levelMap[lvl] -= 1


            if r.left is not None:
                q.append((r.left,lvl+1))
                levelMap[lvl+1] += 1
            if r.right is not None:
                q.append((r.right,lvl+1))
                levelMap[lvl+1] += 1  
        return res
            


        