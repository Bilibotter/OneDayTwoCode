class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-float('inf')]
        l = len(dp)
        count = 0
        for num in nums:
            if num > dp[-1]:
                dp.append(num)
                l = len(dp)
            else:
                for i in range(2, l+1):
                    if num > dp[-i]:
                        dp[-i+1] = num
                        break
        return len(dp) - 1
