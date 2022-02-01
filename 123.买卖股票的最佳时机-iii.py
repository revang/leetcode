#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

"""
author : revang
date   : 2022-02-01
method : 
    1. 贪心: 循环遍历, 求第一段的最大收益和第二段的最大收益（超时）
    2. 动态规划
"""

from typing import List

# @lc code=start

# 贪心
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices or len(prices) == 1:
#             return 0

#         ans = 0
#         for i in range(len(prices)):
#             fst_profit = self.maxProfitOne(prices[0:i+1])  # 第一次最大利润
#             sec_profit = self.maxProfitOne(prices[i+1:])  # 第二次最大利润
#             if fst_profit+sec_profit > ans:
#                 ans = fst_profit+sec_profit
#         return ans

#     def maxProfitOne(self, prices: List[int]) -> int:
#         if not prices or len(prices) == 1:
#             return 0
#         ans = 0
#         min_price = prices[0]  # 截止当前的最低价
#         for i in range(len(prices)):
#             min_price = min(min_price, prices[i])
#             ans = max(ans, prices[i]-min_price)
#         return ans

# 动态规划(单次)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = [[prices[0], 0]]  # [成本(当前最低价格), 收益]
#         for i in range(1, len(prices)):
#             cost = min(res[i-1][0], prices[i])
#             profit = max(res[i-1][1], prices[i]-res[i-1][0])
#             res.append([cost, profit])
#         print(res)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        size = len(prices)
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(size)]  # 结束时的收益=[天数][是否持有股票][卖出次数]
        dp[0][0][0] = 0  # 第1天, 不持有, 卖出0次
        dp[0][0][1] = 0  # 第1天, 不持有, 卖出1次
        dp[0][0][2] = 0  # 第1天, 不持有, 卖出2次
        dp[0][1][0] = -prices[0]  # 第1天, 持有, 卖出0次
        dp[0][1][1] = -prices[0]  # 第1天, 持有, 卖出1次
        dp[0][1][2] = float("-inf")  # 第1天, 持有, 卖出2次(不可能存在) 注: float("-inf")表示负无穷大
        for i in range(1, size):
            dp[i][0][0] = 0  # 第i天, 不持有, 卖出0次
            dp[i][0][1] = max(dp[i-1][0][1], prices[i]+dp[i-1][1][0])  # 第i天, 不持有, 卖出1次
            dp[i][0][2] = max(dp[i-1][0][2], prices[i]+dp[i-1][1][1])  # 第i天, 不持有, 卖出2次

            dp[i][1][0] = max(dp[i-1][1][0], -prices[i]+dp[i-1][0][0])  # 第i天, 持有, 卖出0次
            dp[i][1][1] = max(dp[i-1][1][1], -prices[i]+dp[i-1][0][1])  # 第i天, 持有, 卖出1次
            dp[i][1][2] = float("-inf")  # 第i天, 持有, 卖出2次(不可能存在)
        return max(dp[size-1][0][1], dp[size-1][0][2], 0)


# @lc code=end


def test():
    assert Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
