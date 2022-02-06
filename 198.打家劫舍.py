#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

from typing import List
# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        prepre, pre = 0, 0
        for i in range(len(nums)):
            cur = max(pre, prepre+nums[i])
            prepre = pre
            pre = cur
        return cur

# @lc code=end


def test():
    assert Solution().rob([1, 2, 3, 1]) == 4
