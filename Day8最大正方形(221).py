class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        prev = [1 if i == '1' else 0 for i in matrix[0]] 
        maxi = 1 if 1 in prev else 0
        for line in matrix[1:]:
            now = collections.deque()
            dp = collections.deque()
            update = False
            for i, j in zip(prev, line):
                if j == '1':
                    val = i + 1
                else:
                    val = 0
                if not update:
                    ll = len(dp)
                    if val > maxi:
                        dp.append(val)
                        ll += 1
                    else:
                        dp = collections.deque()
                    if ll > maxi:
                        maxi = ll
                        update = True
                now.append(val)
            prev = now
        return maxi * maxi
