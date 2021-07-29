class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        v, h = len(grid), len(grid[0])
        def draws(grid, start):
            i, j = start
            if grid[i][j] == "":
                return 0
            stack = [start]
            area = 0
            while stack:
                i,j = stack.pop()
                if grid[i][j] == "":
                    continue
                else:
                    grid[i][j] = ""
                    area += 1
                if i + 1 < v and grid[i+1][j] == 1:
                    stack.append((i+1, j))
                if i -1 >= 0 and grid[i-1][j] == 1:
                    stack.append((i-1, j))
                if j + 1 < h and grid[i][j+1] == 1:
                    stack.append((i, j+1))
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    stack.append((i, j-1))
            return area
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x = draws(grid, (i,j))
                    ans = max(ans, x)
        return ans
        
