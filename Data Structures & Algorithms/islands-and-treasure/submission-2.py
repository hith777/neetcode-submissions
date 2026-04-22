class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q:
            r, c, val = q.popleft()
            dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for dr, dc in dirs:
                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 2147483647:
                    grid[dr][dc] = val + 1
                    q.append((dr, dc, grid[dr][dc]))
        
