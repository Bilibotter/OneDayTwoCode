class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [1]
        idx = False
        maxium = -float('inf')
        for i, num in enumerate(nums):
            pct = num * dp[-1]
            if pct < 0:
                if idx:
                    maxium = max(pct//dp[idx], maxium)
                else:
                    idx = i + 1
            else:
                maxium = max(maxium, pct)
                if not pct:
                    pct = 1
                    idx = False
            dp.append(pct)
        return maxium
            


