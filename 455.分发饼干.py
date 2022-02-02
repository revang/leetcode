#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

"""
author : revang
date   : 2022-02-02
method : 贪心
    1. 喂饱饥饿度最小的孩子, 以此类推
"""
from typing import List

# @lc code=start


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        children = sorted(g)
        cookies = sorted(s)
        child_idx, cookie_idx = 0, 0
        while child_idx < len(children) and cookie_idx < len(cookies):
            if children[child_idx] <= cookies[cookie_idx]:
                child_idx += 1
            cookie_idx += 1
        return child_idx


# @lc code=end

def test():
    assert Solution().findContentChildren([1, 2, 3], [1, 1]) == 1
    assert Solution().findContentChildren([1, 2], [1, 2, 3]) == 2
