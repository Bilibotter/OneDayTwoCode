class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort(reverse=True)
        while candidates and candidates[0] > target:
            candidates.pop(0)
        if not candidates:
            return res
        def helper(stack, his, target):
            prev = -1
            limit = len(stack) - 1
            for i, ele in enumerate(stack):
                if ele == prev:
                    continue
                if ele > target:
                    pass
                elif ele == target:
                    h = his.copy()
                    h.append(ele)
                    if h not in res:
                        res.append(h)
                elif ele < target and i < limit:
                    h = his.copy()
                    h.append(ele)
                    helper(stack[i+1:], h, target-ele)
                prev = ele
        helper(candidates, [], target)
        return res
