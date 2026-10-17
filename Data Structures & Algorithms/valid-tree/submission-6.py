class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(src, par):
            if src in visit:
                return False
            
            visit.add(src)

            for nbr in adj[src]:
                if nbr != par:
                    if not dfs(nbr, src):
                        return False
            
            return True


        return dfs(0, -1) and len(visit) == n