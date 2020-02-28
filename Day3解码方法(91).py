class Solution(object):
    def numDecodings(self, s):
        if not s or s.startswith('0'):
            return 0
        dp = [1]
        prev = '3'
        for i, ch in enumerate(s):
            if ch == '0':
                if prev == '0' or int(prev+ch) > 26:
                    return 0
                # 0粘合
                dp.append(dp[i-1])
            elif prev == '0' or int(prev+ch) > 26:
                dp.append(dp[i])
            else:
                dp.append(dp[i] + dp[i-1])
            prev = ch
        print(s, dp)
        return dp[-1]
s = Solution()
print(s.numDecodings('110'))
print(s.numDecodings('101'))
print(s.numDecodings('12'))
print(s.numDecodings('226'))
print(s.numDecodings('1221'))
