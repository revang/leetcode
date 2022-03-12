#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# 状态转移方程: dp[i]=min(min(dp[i-2])+cost[i-2],min(dp[i-1])+cost[i-1])

from typing import List

# @lc code=start


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [0]*(size+1)
        for i in range(2, size+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        return dp[-1]

# @lc code=end


def test():
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
