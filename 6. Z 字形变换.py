"""
执行用时：40 ms, 在所有 Python3 提交中击败了99.75%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了31.09%的用户
通过测试用例：1157 / 1157
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s
        stk = [""] * numRows
        rev = numRows - 2
        span = numRows + rev
        stk = [c for c in s[:numRows]]
        i = 0
        for c in s[numRows:]:
            if i == span:
                i = 0
            if i < rev:
                stk[-2-i] += c
            else:
                stk[i-rev] += c
            i += 1
        return "".join(stk)