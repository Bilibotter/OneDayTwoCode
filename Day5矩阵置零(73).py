# 击败99.85%
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        vet, hor = set(), set() 
        for i,line in enumerate(matrix):
            for j, ele in enumerate(line):
                if ele == 0:
                    hor.add(i)
                    vet.add(j)
        temp = [0 for _ in range(n)] if hor else None
        for h in hor:
            matrix[h] = temp
        for v in vet:
            for i in range(m):
                matrix[i][v] = 0
