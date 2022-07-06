"""
执行用时：
80 ms, 在所有 Python3 提交中击败了96.56%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了71.16%的用户
"""
class Solution:
    def characterReplacement(self, s: str, k: int):
        dic = {chr(i) : 0 for i in range(65, 91)}
        left, maxi, ret = 0, 0, 0
        for right, c in enumerate(s):
            dic[c] += 1
            maxi = max(dic[c], maxi)
            if right + 1 - left - maxi > k:
                dic[s[left]] -= 1 
                left += 1
            else:
                ret = right + 1 - left
        return ret
        
