#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start

# 动态规划
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [[0] for _ in range(n)]
#         for i in range(n):
#             if i < 2:
#                 dp[i] = i+1
#             else:
#                 dp[i] = dp[i-2]+dp[i-1]
#         return dp[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prepre, pre = 1, 2
        for _ in range(3, n+1):
            cur = prepre+pre
            prepre = pre
            pre = cur
        return cur

# @lc code=end


def test():
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
