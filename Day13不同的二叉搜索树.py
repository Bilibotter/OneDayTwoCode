# dp写得是真烂！
class Solution:
    def numTrees(self, n):
        dp = {1:1, 2:2, 3:5}
        if n < len(dp):
            return dp[n]
        for i in range(4, n+1):
            num = 0
            for j in range(1, i-1):
                num += dp[j] * dp[i-j-1]
            num += 2 * dp[i-1]
            dp[i] = num
        return dp[n]
