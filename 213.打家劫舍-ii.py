#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

from typing import List

# @lc code=start

""" 状态转移方程: dp[i]=max(dp[i-1],dp[i-2]+nums[i])
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
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
    Solution().rob([2, 3, 2]) == 3
    Solution().rob([1, 2, 3, 1]) == 4
    Solution().rob([1, 2, 3]) == 3
    Solution().rob([1]) == 1
