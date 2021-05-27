# 在所有 Python3 提交中击败了91.94%的用户
class Solution:
    def maxProfit(self, prices) -> int:
        buy = float('inf')
        maxProfits = 0
        for price in prices:
            if price < buy:
                buy = price
            else:
                maxProfits = max(maxProfits, price - buy)
        return maxProfits
