#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

from typing import List

# @lc code=start


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        begin, end = 0, len(s)-1
        while begin < end:
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1

# @lc code=end
