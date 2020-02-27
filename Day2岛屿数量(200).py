class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        islands = 0
        deepth = len(grid)
        width = len(grid[0])
        limit = [deepth-1, width-1]
        def helper(i, j):
            grid[i][j] = 'u'
            if i > 0:
                if grid[i-1][j]== '1':
                    helper(i-1, j)
            if j > 0:
                if grid[i][j-1] == '1':
                    helper(i, j-1)
            if i < limit[0]:
                if grid[i+1][j] == '1':
                    helper(i+1, j)
            if j < limit[1]:
                if grid[i][j+1] == '1':
                    helper(i, j+1)
        for i in range(deepth):
            for j in range(width):
                if grid[i][j] == '1':
                    islands += 1
                    helper(i, j)
        return islands
        
            
