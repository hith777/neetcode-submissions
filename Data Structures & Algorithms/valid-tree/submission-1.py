class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for i in range(n)]

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)

            for nbr in adj[node]:
                if nbr == par:
                    continue
                if not dfs(nbr, node):
                    return False
            
            return True


        return dfs(0, -1) and len(visit) == n