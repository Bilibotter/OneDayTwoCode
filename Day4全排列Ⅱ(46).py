# 超级傻逼超级慢的解
class Solution(object):
    def permuteUnique(self, nums):
        r = []
        dic = {}
        def helper(arr, lst, his):
            for i, ele in enumerate(arr):
                l = lst.copy()
                l.append(ele)
                h = his + str(ele)
                if len(arr) != 1:
                    helper(arr[:i]+arr[i+1:], l, h)
                elif dic.get(h, 0) == 0:
                    dic[h] = 1
                    r.append(l)
        helper(nums, [], '')
        return r
 
# 抄了击败96%的解，击败99%
class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        def helper(nums, his):
            pv = ''
            if len(nums) == 1:
                res.append(his+nums)
                return
            for i, n in enumerate(nums):
                if n == pv:
                    continue
                helper(nums[:i]+nums[i+1:], his+[n])
                pv = n
        helper(nums, [])
        return res
                    
