"""
执行用时：28 ms, 在所有 Python3 提交中击败了98.79%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.04%的用户
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = [[]]
        def dfs(current, index):
            if len(current) == index+1:
                current.append(nums[index])
                s.append(current)
                return
            prev = None
            bound = len(nums) - 1
            for i, num in enumerate(nums[index:]):
                if num == prev:
                    continue
                curr = current.copy()
                curr.append(num)
                s.append(curr)
                if i + index < bound:
                    dfs(curr, i+index+1)
                prev = num
        dfs([], 0)
        return s