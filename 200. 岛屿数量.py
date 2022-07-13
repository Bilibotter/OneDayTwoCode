class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        h, w= len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i == h or j == w:
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for span in (1, -1):
                dfs(i+span, j)
                dfs(i, j+span)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        return res
