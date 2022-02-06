#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

from typing import List

# @lc code=start
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        stack = deque()
        for idx in range(size):
            while stack:
                pre_idx = stack[-1]
                if temperatures[idx] <= temperatures[pre_idx]:
                    break
                stack.pop()
                res[pre_idx] = idx-pre_idx
            stack.append(idx)
        return res

# @lc code=end


def test():
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]
