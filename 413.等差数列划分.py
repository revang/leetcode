#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

from typing import List

# @lc code=start


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        size = len(nums)
        dp = [0] * size
        for i in range(1, size-1):
            if nums[i]-nums[i-1] == nums[i+1]-nums[i]:
                dp[i] = dp[i-1]+1
        return sum(dp)

# @lc code=end


def test():
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5]) == 6
