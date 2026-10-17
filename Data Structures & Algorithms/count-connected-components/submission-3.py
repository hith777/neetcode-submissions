class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(src, par):
            if src in visit:
                return
            
            visit.add(src)

            for nbr in adj[src]:
                if nbr != par:
                    dfs(nbr, src)


        
        components = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                components += 1
        
        return components