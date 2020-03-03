class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        max1, max0, prev1, prev2 = 0, 0, 0, 0
        for num in nums[1:]:
            max1, prev1 = max(max1, prev1+num), max1
        for num in nums[:-1]:
            max0, prev2 = max(max0, prev2+num), max0
        return max(max1, max0)
        
