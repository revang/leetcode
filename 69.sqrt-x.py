#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

"""
author : revang
date   : 2022-02-02
method : 二分查找
"""

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 1, x
        while left <= right:
            mid = (left+right)//2
            if x == mid*mid:
                return mid
            elif x > mid*mid:
                left = mid+1
            else:
                right = mid-1
        return right

# @lc code=end


def test():
    assert Solution().mySqrt(2) == 1
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
