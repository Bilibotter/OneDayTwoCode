class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        tower = [[0] * k for k in range(1, query_row+2)]
        bound = len(tower) - 1
        tower[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                overflow = (tower[i][j]-1.0)/2.0
                if overflow > 0 and i < bound:
                    tower[i+1][j] += overflow
                    tower[i+1][j+1] += overflow
        return min(1, tower[query_row][query_glass])