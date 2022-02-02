#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
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
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key=itemgetter(1, 0))
        count, pre, size = 1, points[0][1], len(points)
        for i in range(1, size):
            if pre < points[i][0]:
                count += 1
                pre = points[i][1]
        return count


# @lc code=end

def test():
    assert Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert Solution().findMinArrowShots([[1, 2]]) == 1
    assert Solution().findMinArrowShots([[2, 3], [2, 3]]) == 1
