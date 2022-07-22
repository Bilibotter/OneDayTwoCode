"""
执行用时：40 ms, 在所有 Python3 提交中击败了94.58%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了70.78%的用户
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for num in asteroids:
            alive = True
            while res and res[-1] > 0:
                if num > 0:
                    break
                elif -num <= res[-1]:
                    alive = False
                    if -num == res[-1]:
                        res.pop()
                    break
                else:
                    res.pop()
            if alive:
                res.append(num)
        return res