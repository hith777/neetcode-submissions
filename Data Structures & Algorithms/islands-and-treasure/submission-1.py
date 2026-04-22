class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = deque([])
        visit = set()

        def addCell(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == -1 or (r, c) in visit:
                return
            q.append((r, c))
            visit.add((r, c))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        val  = 0
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = val
                nbrs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in nbrs:
                    addCell(nr, nc)
            val += 1
