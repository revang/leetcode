#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

"""
author : revang
date   : 2022-02-02
method : 贪心-区间问题
"""

from typing import List

# @lc code=start
from operator import itemgetter


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=itemgetter(1, 0))
        # intervals = sorted(intervals, key=lambda x: x[1])
        count, pre = 0, intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < pre:
                count += 1
            else:
                pre = intervals[i][1]
        return count

# @lc code=end


def test():
    assert Solution().eraseOverlapIntervals([[1, 3], [2, 4]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 3], [3, 5], [3, 4], [4, 5]]) == 1
