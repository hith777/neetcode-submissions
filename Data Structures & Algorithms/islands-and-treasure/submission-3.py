class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        

        while q:
            r, c, val = q.popleft()
            nbrs = [(r + 0, c + 1), (r + 1, c + 0), (r - 1, c + 0), (r + 0, c - 1)]

            for nr, nc in nbrs:
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = val + 1
                    q.append((nr, nc, val + 1))
