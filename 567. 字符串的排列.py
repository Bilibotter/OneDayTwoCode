"""
执行结果：通过
执行用时：56 ms, 在所有 Python3 提交中击败了96.39%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了12.65%的用户
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        zero = {chr(i): 0 for i in range(97, 123)}
        match = zero.copy()
        for c1, c2 in zip(s1, s2[:len(s1)]):
            match[c1] += 1
            zero[c2] += 1
        if match == zero:
            return True
        keys = set(s1)
        for i in range(len(s2) - len(s1)):
            c = s2[len(s1) + i]
            zero[c] += 1
            zero[s2[i]] -= 1
            if c in keys and zero == match:
                return True
        return False


