#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

"""
author : revang
date   : 2022-02-02
method : 贪心(在每次遍历中, 只考虑相邻一侧的大小关系)
    1. 初始化全部更新为1
    2. 从左往右遍历, 如果左边孩子的评分比右边高, 左边孩子的糖果数加1
    2. 从右往左遍历, 如果左边孩子的评分比右边低，左边孩子的糖果数=max(左边孩子的糖果数, 右边孩子糖果数+1)
"""

from typing import List

# @lc code=start


class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        if size < 2:
            return size

        nums = [1]*len(ratings)
        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1]+1
        for i in range(size-1, 0, -1):  # sorted(range(1, size), reverse=True)
            if ratings[i] < ratings[i-1]:
                nums[i-1] = max(nums[i-1], nums[i]+1)
        return sum(nums)

# @lc code=end


def test():
    assert Solution().candy([1, 0, 2]) == 5
    assert Solution().candy([1, 2, 2]) == 4
