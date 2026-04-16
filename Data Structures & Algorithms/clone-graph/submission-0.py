"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from queue import Queue

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is  None:
            return None
        q = Queue()

        q.put(node)
        root = Node(node.val)
        cloned = {}
        cloned[node] = root


        while not q.empty():
            curr = q.get()

            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    childNode = Node(neighbor.val)
                    cloned[neighbor] = childNode
                    q.put(neighbor)
                cloned[curr].neighbors.append(cloned[neighbor]) 


        return root