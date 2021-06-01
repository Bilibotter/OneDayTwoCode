# 在所有 Python3 提交中击败了83.60%的用户
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            count = num + max(dp[-2], dp[-3])
            dp.append(count)
        return max(dp[-1], dp[-2])
