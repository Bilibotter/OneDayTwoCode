class Solution:
    def kConcatenationMaxSum(self, arr, k):
        t = 0
        count = 0
        max_dp = 0
        max_left = 0
        for i in arr:
            if i > 0:
                t += i
            elif not t:
                pass
            else:
                max_left = max(max_left, count)
                max_dp = max(t, max_dp)
                t = max(t+i, 0)
            count += i
        max_left = max(max_left, count)
        max_dp = max(t, max_dp)
        if k > 1:
            sums = max(count, max_dp) + count * (k - 1)
            return max(max_dp, t + max_left, sums)% 1000000007
        return max_dp% 1000000007
