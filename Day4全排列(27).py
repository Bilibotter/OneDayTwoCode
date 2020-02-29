# 击败84%
class Solution(object):
    def permute(self, nums):
        res = []
        def helper(nums, his):
            if len(nums) == 1:
                res.append(his+nums)
                return
            for i, num in enumerate(nums):
                n = nums.copy()
                n.pop(i)
                helper(n, his+[num])
        helper(nums, [])
        return res
                
