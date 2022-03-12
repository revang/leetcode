#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

from typing import List

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for i in nums:
            pre = max(pre+i, i)
            ans = max(ans, pre)
        return ans


# @lc code=end
