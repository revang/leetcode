#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0 or s[0] == "0":
            return 0
        if size == 1:
            return 1
        if size >= 2 and s[1] == "0" and int(s[0]+s[1]) >= 30:
            return 0

        dp = [0]*(size)
        dp[0] = 1
        dp[1] = 2 if int(s[1]) != 0 and int(s[0]+s[1]) <= 26 else 1
        for i in range(2, size):
            if int(s[i-1]) == 0 and int(s[i]) == 0:
                return 0
            if int(s[i-1]) == 0 or int(s[i]) == 0:
                if int(s[i-1]+s[i]) >= 30:
                    return 0
                dp[i] = min(dp[i-2], dp[i-1])
            elif int(s[i-1]+s[i]) > 26:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-2]+dp[i-1]
        return dp[-1]
        # @lc code=end


def test():
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("9") == 1
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("0") == 0
    assert Solution().numDecodings("10") == 1
    assert Solution().numDecodings("1010") == 1
    assert Solution().numDecodings("1") == 1
    assert Solution().numDecodings("2101") == 1
    assert Solution().numDecodings("10011") == 0
    assert Solution().numDecodings("230") == 0
    assert Solution().numDecodings("301") == 0
    assert Solution().numDecodings("1201234") == 3
