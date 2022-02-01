#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

"""
author : revang
date   : 2022-02-01
method : 双指针
"""

# @lc code=start
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            val = left*left+right*right
            if val == c:
                return True
            elif val < c:
                left += 1
            else:
                right -= 1
        return False

# @lc code=end


def test():
    assert Solution().judgeSquareSum(5) == True
    assert Solution().judgeSquareSum(3) == False
    assert Solution().judgeSquareSum(4) == True
    assert Solution().judgeSquareSum(100000000) == True
