"""
执行用时：424 ms, 在所有 Python3 提交中击败了98.27%的用户
内存消耗：18.1 MB, 在所有 Python3 提交中击败了11.77%的用户
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        prev = float('inf')
        nums.sort()
        bound = len(nums)-1
        for i,first in enumerate(nums):
            if prev == first:
                continue
            if first > 0:
                break
            while first * 2 + nums[bound] > 0 and bound > i:
                bound -= 1
            l, r = i+1, bound
            while l < r:
                curr = first + nums[l] + nums[r]
                if curr == 0:
                    maybe = [first, nums[l], nums[r]]
                    if not res:
                        res.append(maybe)
                    elif maybe != res[-1]:
                        res.append(maybe)
                elif curr > 0:
                    l -= 1
                    r -= 1
                l += 1
            prev = first
        return res