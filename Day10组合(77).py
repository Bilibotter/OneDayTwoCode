class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        res = []
        def helper(prev, start, limit, remain):
            if remain == 0:
                res.append(prev)
                return
            for i in range(start, limit-remain+2):
                p = prev.copy()
                p.append(i)
                helper(p, i+1, limit, remain-1)

        helper([], 1, n, k)
        return res
