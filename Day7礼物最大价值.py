class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = grid.copy()
        count = 0
        for i in range(m):
            count += dp[i][0]
            dp[i][0] = count
        count = 0
        for i, ele in enumerate(dp[0]):
            count += ele
            dp[0][i] = count
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
