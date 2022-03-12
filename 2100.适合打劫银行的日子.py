#
# @lc app=leetcode.cn id=2100 lang=python3
#
# [2100] 适合打劫银行的日子
#

from typing import List

# @lc code=start


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        size = len(security)
        left = [0]*size
        right = [0]*size
        for i in range(1, size):
            if security[i] <= security[i-1]:
                left[i] = left[i-1]+1
            if security[size-i-1] <= security[size-i]:
                right[size-i-1] = right[size-i]+1
        return [i for i in range(time, size-time) if left[i] >= time and right[i] >= time]

# @lc code=end


def test():
    assert Solution().goodDaysToRobBank([5, 3, 3, 3, 5, 6, 2], 2) == [2, 3]
