#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

from typing import List

# @lc code=start

"""
author : revang
date   : 2022-02-02
method : 二分查找
    1. 求左边界: 向下取整，等号归右，左加一
    2. 求右边界: 向上取整，等号归左，右减一
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        lower = self.lower_bound(nums, target)
        upper = self.upper_bound(nums, target)
        return [lower, upper]

    def lower_bound(self, nums, target):
        """ 求左边界 """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) >> 1  # 向下取整
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        return left if nums[left] == target else -1

    def upper_bound(self, nums, target):
        """ 求右边界 """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right+1) >> 1  # 向上取整
            if nums[mid] <= target:
                left = mid
            else:
                right = mid-1
        return right if nums[right] == target else -1

# @lc code=end


def test():
    assert Solution().lower_bound([5, 7, 7, 8, 8, 10], 8) == 3
    assert Solution().upper_bound([5, 7, 7, 8, 8, 10], 8) == 4
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().lower_bound([5, 7, 7, 8, 8, 10], 6) == -1
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert Solution().lower_bound([1], 1) == 0
    assert Solution().upper_bound([1], 1) == 0
    assert Solution().lower_bound([2, 2], 2) == 0
    assert Solution().upper_bound([2, 2], 2) == 1
