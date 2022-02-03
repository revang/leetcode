#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

from typing import List

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height)-1
        while left < right:
            v = min(height[left], height[right])*(right-left)
            ans = max(ans, v)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

# @lc code=end
