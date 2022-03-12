#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

from typing import List

# @lc code=start

# 状态转移方程: dp[i]=max(dp[i-1],dp[i-2]+nums[i])


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, size):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

# @lc code=end


def test():
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([0]) == 0
