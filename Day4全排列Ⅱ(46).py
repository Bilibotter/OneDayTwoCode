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
