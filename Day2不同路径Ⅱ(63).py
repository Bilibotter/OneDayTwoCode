# 一次击败96%,一次98%，取96%
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        res = [[1 for __ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i, l in enumerate(obstacleGrid[0]):
            if l == 1:
                for j in range(i, len(obstacleGrid[0])):
                    res[0][j] = 0
                break
        for i in range(len(res)):
            if obstacleGrid[i][0] == 1:
                for j in range(i, len(res)):
                    res[j][0] = 0
                break
        for i, line in enumerate(obstacleGrid):
            for j, l in enumerate(line):
                if l == 1:
                    res[i][j] = 0
                elif i * j == 0:
                    continue
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]
