# 这么脑残的解都能击败98%
# 果然大家都是懒人
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        res = [[0 for _ in range(n)] for __ in range(n)]
        width = n
        l, r = 0, n-1
        num = 1
        while width > 1:
            for i in range(width):
                res[l][l+i] = num
                num += 1
            num -= 1
            for i in range(width):
                res[l+i][r] = num
                num += 1
            num -= 1
            for i in range(width):
                res[r][r-i] = num
                num += 1
            num -= 1
            for i in range(width-1):
                res[r-i][l] = num
                num += 1
            l += 1
            r -= 1  
            width -= 2
        if width == 1:
            mid = int((n-1)/2)
            res[mid][mid] = n * n
        return res
