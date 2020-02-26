# 加入细节优化，击败93%
class Solution(object):
    def subsets(self, nums):
        r = []
        def recursive(nums, prev):
            for i, num in enumerate(nums[:-1]):
                temp = prev + [num]
                r.append(temp)
                recursive(nums[i+1:], temp)
            r.append(prev+[nums[-1]])
        recursive(nums, prev=[])
        return r + [[]]
# 击败80%
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def recursive(nums, prev):
            length = len(nums)
            for i, num in enumerate(nums):
                temp = prev + [num]
                res.append(temp)
                if i+1 < length:
                    recursive(nums[i+1:], temp)
        recursive(nums, prev=[])
        return res + [[]]
