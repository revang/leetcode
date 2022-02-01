#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

"""
author : revang
date   : 2022-01-31
method : 贪心
    1. 循环遍历, 假设以当前价格卖出, 那么最大利润=当前价格-截止当前的最低价。
    2. 截止当前的最低价可以用一个变量记录，不用循环遍历
"""

from typing import List

# @lc code=start


# 动态规划（超时）
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ans = 0
#         for i in range(len(prices)):
#             val = max(prices[i:])-prices[i]
#             ans = max(ans, val)
#         return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        ans = 0
        min_price = prices[0]  # 截止当前的最低价
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            ans = max(ans, prices[i]-min_price)
        return ans

# @lc code=end


def test():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
