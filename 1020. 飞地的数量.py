class Solution:
    def numEnclaves(self, grid):
        h, w = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i == h or j == w:
                return
            if not grid[i][j]:
                return
            grid[i][j] = 0
            for span in (-1, 1):
                dfs(i+span, j)
                dfs(i, j+span)
        for i in range(h):
            dfs(i, 0)
            dfs(i, w-1)
        for j in range(w):
            dfs(0, j)
            dfs(h-1, j)
        return sum([sum(row) for row in grid[1:-1]])