from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}

        def dfs(current):

            if current in clones:
                return clones[current]

            clone = Node(current.val)

            clones[current] = clone

            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)