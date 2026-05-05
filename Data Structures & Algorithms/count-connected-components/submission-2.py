class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)

            for nbr in adj[node]:
                dfs(nbr)

        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count
