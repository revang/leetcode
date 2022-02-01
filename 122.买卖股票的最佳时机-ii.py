#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

"""
author : revang
date   : 2022-01-31
method : 贪心
    1. 如果第二天的价格笔第一天高就卖出
"""

from typing import List

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            val = prices[i]-prices[i-1]
            if val > 0:
                ans = ans+val
        return ans

# @lc code=end


def test():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
