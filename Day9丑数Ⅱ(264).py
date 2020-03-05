class Solution:
    def nthUglyNumber(self, n: int) -> int:
        idx2 = 0
        idx3 = 0
        idx5 = 0
        lst = [1]
        num2 = 2
        num3 = 3
        num5 = 5
        while len(lst) < n:
            minium = min(num2, num3, num5)
            if minium == num2:
                if minium > lst[-1]:
                    lst.append(num2)
                idx2 += 1
                num2 = lst[idx2] * 2
            elif minium == num3:
                idx3 += 1
                if minium > lst[-1]:
                    lst.append(num3)
                num3 = lst[idx3] * 3
            else:
                idx5 += 1
                if minium > lst[-1]:
                    lst.append(num5)
                num5 = lst[idx5] * 5
        return lst[-1]
