# 只击败85%
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
# 取消dp后，击败98%
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev = 1
        maxium, minium = -float('inf'), -1
        neg = False
        for num in nums:
            pct = num * prev
            if pct > 0:
               maxium = max(maxium, pct)
            elif pct < 0:
                if neg:
                    maxium = max(maxium, pct//neg)
                else:
                    neg = pct
            else:
                maxium = max(maxium, 0)
                neg = False
                pct = 1
            prev = pct
           
        return maxium
            

            


