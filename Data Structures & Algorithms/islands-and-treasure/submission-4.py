class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        

        while q:
            r, c = q.popleft()

            directions = [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]

            for dr, dc in directions:
                if 0 <= dr < ROWS and 0 <= dc < COLS and grid[dr][dc] > grid[r][c] + 1:
                    grid[dr][dc] = grid[r][c] + 1
                    q.append((dr, dc))

