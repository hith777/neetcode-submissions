class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        
        def dfs(node, par):
            if node in visit:
                return 
            
            visit.add(node)

            for nbr in adj[node]:
                if nbr == par:
                    continue
                dfs(nbr, node)

            return


        count = 0

        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                count += 1
        
        return count
            